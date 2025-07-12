"""
Data Router Module
==================

This module defines the data API router that handles file upload and data
processing endpoints. It provides the core functionality for the RAG system's
file handling capabilities including validation, storage, and error handling.

Dependencies:
- fastapi: For API router, file uploads, and dependency injection
- os: For file system operations
- helpers.config: For application settings and dependency injection
- controllers: For data and project controller functionality
- aiofiles: For asynchronous file operations
- models.ResponseSignals: For standardized response messages
- logging: For error logging

Used by:
- main.py: Included in the main FastAPI application
"""

from fastapi import FastAPI, APIRouter, Depends, UploadFile, status
from fastapi.responses import JSONResponse
import os
from helpers.config import get_settings, Settings
from controllers import DataController, ProjectController
import aiofiles
from models import ResponseSignals
import logging

# Set up logging for error tracking
logger = logging.getLogger('uvicorn.error')

# Create data router with API version prefix and tags
data_router = APIRouter(
    prefix="/api/v1/data",
    tags=["api_v1", "data"],
)

@data_router.post("/upload/{project_id}")
async def upload_data(project_id: str, file: UploadFile,
                      app_settings: Settings = Depends(get_settings)):
    """
    File upload endpoint for RAG system
    
    This endpoint handles file uploads for the RAG system, including
    validation, storage, and error handling. It processes uploaded files
    and stores them in project-specific directories with unique names.
    
    Args:
        project_id (str): Unique identifier for the project
        file (UploadFile): The uploaded file from the request
        app_settings (Settings): Application settings injected by FastAPI
    
    Returns:
        JSONResponse: Success or error response with appropriate status code
    
    Used by:
        - main.py: Included in the data_router for file upload functionality
        - External clients: For uploading files to the RAG system
    
    Dependencies:
        - DataController: For file validation and path generation
        - ProjectController: For project directory management
        - helpers/config.py -> Settings: For configuration access
        - models.ResponseSignals: For standardized response messages
    """
    
    # Initialize data controller for file processing
    # Used by: controllers/DataController.py
    data_controller = DataController()

    # Validate the uploaded file for type and size compliance
    # Used by: DataController.validate_uploaded_file()
    is_valid, result_signal = data_controller.validate_uploaded_file(file=file)

    # Return error response if validation fails
    if not is_valid:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "signal": result_signal
            }
        )

    # Get project directory path for file storage
    # Used by: ProjectController.get_project_path()
    project_dir_path = ProjectController().get_project_path(project_id=project_id)
    
    # Generate unique file path and file ID
    # Used by: DataController.generate_unique_filepath()
    file_path, file_id = data_controller.generate_unique_filepath(
        orig_file_name=file.filename,
        project_id=project_id
    )

    try:
        # Write the uploaded file to disk using asynchronous file operations
        # Used by: aiofiles for async file handling
        async with aiofiles.open(file_path, "wb") as f:
            # Read file in chunks and write to disk
            # Used by: helpers/config.py -> Settings.FILE_DEFAULT_CHUNK_SIZE
            while chunk := await file.read(app_settings.FILE_DEFAULT_CHUNK_SIZE):
                await f.write(chunk)
    except Exception as e:
        # Log error for debugging purposes
        logger.error(f"Error while uploading file: {e}")

        # Return error response for upload failure
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "signal": ResponseSignals.FILE_UPLOADED_FAIL.value
            }
        )

    # Return success response with file ID
    return JSONResponse(
            content={
                "signal": ResponseSignals.FILE_UPLOAD_SUCCESS.value,
                "file_id": file_id
            }
        )