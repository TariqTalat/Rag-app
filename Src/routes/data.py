from fastapi import FastAPI, APIRouter, Depends, UploadFile
import os
from helpers.config import get_settings, Settings
from controllers import DataController

data_router = APIRouter(prefix="/data",tags=["data"]) # Create a new router instance with a prefix and tags

@data_router.post("/upload/{Project_id}") # Define a route for the root path

async def upload_data(Project_id: str, file: UploadFile,
                    app_settings: Settings = Depends(get_settings)):
    """
    Upload a file to the server.
    
    Args:
        Project_id (str): The ID of the project to which the file belongs.
        file (UploadFile): The file to be uploaded.
    
    Returns:
        dict: A dictionary containing the project ID and the filename.
    """
    is_valid = DataController().validate_upload_file(file=file)
    return is_valid
