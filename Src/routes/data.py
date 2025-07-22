"""
Data Router Module
==================

Stepwise Breakdown:
-------------------
1. Import FastAPI, APIRouter, dependencies, and controllers.
2. Create the data_router for file upload and processing endpoints.
3. Define the upload_data endpoint for file uploads.
4. Define the process_endpoint for file chunking and processing.

This module defines the API router for data-related endpoints, including
file upload and file processing (chunking) for the mini-RAG application.

Dependencies:
- fastapi: For API router, request, and dependency injection
- aiofiles: For asynchronous file operations
- logging: For error logging
- controllers: For business logic
- models: For response signals and data models
- .schemes.data: For request validation schema
"""

from fastapi import FastAPI, APIRouter, Depends, UploadFile, status, Request
from fastapi.responses import JSONResponse
import os
from helpers.config import get_settings, Settings
from controllers import DataController, ProjectController, ProcessController
import aiofiles
from models import ResponseSignals
import logging
from .schemes.data import ProcessRequest
from models.ProjectModel import ProjectModel
from models.ChunkModel import ChunkModel
from models.db_schemes import DataChunk

logger = logging.getLogger('uvicorn.error')

# Step 1: Create data router with API version prefix and tags
data_router = APIRouter(
    prefix="/api/v1/data",
    tags=["api_v1", "data"],
)

@data_router.post("/upload/{project_id}")
async def upload_data(request: Request, project_id: str, file: UploadFile,
                      app_settings: Settings = Depends(get_settings)):
    """
    Upload Data Endpoint
    --------------------
    Handles file uploads for a given project. Validates file type and size, saves the file,
    and returns a success or error signal.

    Args:
        request (Request): FastAPI request object (for db access)
        project_id (str): The project identifier
        file (UploadFile): The uploaded file
        app_settings (Settings): Application settings (injected)
    Returns:
        JSONResponse: Signal and file ID on success, or error signal on failure

    Example usage (with FastAPI TestClient):
        >>> from fastapi.testclient import TestClient
        >>> from main import app
        >>> client = TestClient(app)
        >>> with open('test.txt', 'rb') as f:
        ...     response = client.post('/api/v1/data/upload/proj1', files={'file': f})
        >>> response.json()
        {'signal': 'file uploaded successfully', 'file_id': '...'}
    """
    # Step 1: Get or create the project
    project_model = await ProjectModel.create_instance(db_client=request.app.db_client)
    project = await project_model.get_project_or_create_one(project_id=project_id)
    # Step 2: Validate the file properties
    data_controller = DataController()
    is_valid, result_signal = data_controller.validate_uploaded_file(file=file)
    if not is_valid:
        # Step 3: Return error if validation fails
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"signal": result_signal}
        )
    # Step 4: Generate file path and save file
    project_dir_path = ProjectController().get_project_path(project_id=project_id)
    file_path, file_id = data_controller.generate_unique_filepath(
        orig_file_name=file.filename,
        project_id=project_id
    )
    try:
        # Step 5: Write file in chunks asynchronously
        async with aiofiles.open(file_path, "wb") as f:
            while chunk := await file.read(app_settings.FILE_DEFAULT_CHUNK_SIZE):
                await f.write(chunk)
    except Exception as e:
        # Step 6: Log error and return failure signal
        logger.error(f"Error while uploading file: {e}")
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"signal": ResponseSignals.FILE_UPLOAD_FAILED.value}
        )
    # Step 7: Return success signal and file ID
    return JSONResponse(
            content={
                "signal": ResponseSignals.FILE_UPLOAD_SUCCESS.value,
                "file_id": file_id,
            }
        )

@data_router.post("/process/{project_id}")
async def process_endpoint(request: Request, project_id: str, process_request: ProcessRequest):
    """
    Process File Endpoint
    ---------------------
    Processes an uploaded file by splitting it into chunks for a given project.
    Optionally resets previous chunks. Returns a signal and the number of inserted chunks.

    Args:
        request (Request): FastAPI request object (for db access)
        project_id (str): The project identifier
        process_request (ProcessRequest): Request body with file_id, chunk_size, overlap_size, do_reset
    Returns:
        JSONResponse: Signal and number of inserted chunks, or error signal on failure

    Example usage (with FastAPI TestClient):
        >>> from fastapi.testclient import TestClient
        >>> from main import app
        >>> client = TestClient(app)
        >>> body = {'file_id': 'file.txt', 'chunk_size': 100, 'overlap_size': 20, 'do_reset': 1}
        >>> response = client.post('/api/v1/data/process/proj1', json=body)
        >>> response.json()
        {'signal': 'file processing successful', 'inserted_chunks': 10}
    """
    # Step 1: Extract request parameters
    file_id = process_request.file_id
    chunk_size = process_request.chunk_size
    chunk_overlap = process_request.overlap_size
    do_reset = process_request.do_reset
    # Step 2: Get or create the project
    project_model = await ProjectModel.create_instance(db_client=request.app.db_client)
    project = await project_model.get_project_or_create_one(project_id=project_id)
    # Step 3: Process the file content
    process_controller = ProcessController(project_id=project_id)
    file_content = process_controller.get_file_content(file_id=file_id)
    file_chunks = process_controller.process_file_content(
        file_content=file_content,
        file_id=file_id,
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    # Step 4: Return error if no chunks were created
    if file_chunks is None or len(file_chunks) == 0:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"signal": ResponseSignals.FILE_PROCESSING_FAIL.value}
        )
    # Step 5: Prepare chunk records for insertion
    file_chunks_records = [
        DataChunk(
            chunk_text=chunk.page_content,
            chunk_metadata=chunk.metadata,
            chunk_order=i+1,
            chunk_project_id=project.id,
        )
        for i, chunk in enumerate(file_chunks)
    ]
    chunk_model = await ChunkModel.create_instance(db_client=request.app.db_client)
    # Step 6: Optionally reset (delete) previous chunks
    if do_reset == 1:
        _ = await chunk_model.delete_chunks_by_project_id(
            project_id=project.id
        )
    # Step 7: Insert new chunks
    no_records = await chunk_model.insert_many_chunks(chunks=file_chunks_records)
    # Step 8: Return success signal and number of inserted chunks
    return JSONResponse(
        content={
            "signal": ResponseSignals.FILE_PROCESSING_SUCCESS.value,
            "inserted_chunks": no_records
        }
    )