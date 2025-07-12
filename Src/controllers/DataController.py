"""
Data Controller Module
======================

This module handles all data-related operations including file validation,
file upload processing, and file path management. It provides the core
functionality for the RAG system's file handling capabilities.

Dependencies:
- .BaseController: Inherits from BaseController for common functionality
- .ProjectController: For project directory management
- fastapi.UploadFile: For handling file uploads
- models.ResponseSignals: For standardized response messages
- re: For file name cleaning operations
- os: For file system operations

Used by:
- routes/data.py: For file upload endpoint processing
"""

from .BaseController import BaseController
from .ProjectController import ProjectController
from fastapi import UploadFile
from models import ResponseSignals
import re
import os

class DataController(BaseController):
    """
    Data Controller Class
    
    This class handles all data processing operations including file validation,
    file upload management, and file path generation. It extends BaseController
    to inherit common functionality while providing specialized data handling.
    
    Attributes:
        size_scale (int): Conversion factor from MB to bytes (1048576)
    
    Used by:
        - routes/data.py: For processing file uploads in API endpoints
    """
    
    def __init__(self):
        """
        Initialize the data controller with size conversion settings
        
        Sets up the controller with a size scale factor for converting
        between MB and bytes for file size validation.
        """
        # Initialize parent class (BaseController)
        super().__init__()
        
        # Size scale factor: 1 MB = 1048576 bytes
        self.size_scale = 1048576 # convert MB to bytes

    def validate_uploaded_file(self, file: UploadFile):
        """
        Validate uploaded file for type and size compliance
        
        This method checks if the uploaded file meets the application's
        requirements for file type and size limits.
        
        Args:
            file (UploadFile): The uploaded file to validate
        
        Returns:
            tuple: (bool, str) - (is_valid, response_message)
        
        Used by:
            - routes/data.py -> upload_data(): For validating files before upload
        
        Response Signals:
            - FILE_VALIDATE_SUCCESS: File passes all validation checks
            - FILE_TYPE_NOT_SUPPORTED: File type is not in allowed list
            - FILE_SIZE_EXCEEDED: File size exceeds maximum limit
        """
        # Check if file type is in the allowed types list
        # Used by: helpers/config.py -> Settings.FILE_ALLOWED_TYPES
        if file.content_type not in self.app_settings.FILE_ALLOWED_TYPES:
            return False, ResponseSignals.FILE_TYPE_NOT_SUPPORTED.value

        # Check if file size exceeds the maximum allowed size
        # Used by: helpers/config.py -> Settings.FILE_MAX_SIZE
        if file.size > self.app_settings.FILE_MAX_SIZE * self.size_scale:
            return False, ResponseSignals.FILE_SIZE_EXCEEDED.value

        return True, ResponseSignals.FILE_VALIDATE_SUCCESS.value

    def generate_unique_filepath(self, orig_file_name: str, project_id: str):
        """
        Generate a unique file path for uploaded files
        
        This method creates a unique file path by combining a random string
        with the cleaned original file name, ensuring no filename conflicts.
        
        Args:
            orig_file_name (str): Original name of the uploaded file
            project_id (str): ID of the project for directory organization
        
        Returns:
            tuple: (str, str) - (full_file_path, unique_file_name)
        
        Used by:
            - routes/data.py -> upload_data(): For creating unique file paths
        
        Dependencies:
            - self.generate_random_string(): For creating random identifiers
            - ProjectController.get_project_path(): For getting project directory
            - self.get_clean_file_name(): For cleaning the original filename
        """
        # Generate a random key for uniqueness
        # Used by: BaseController.generate_random_string()
        random_key = self.generate_random_string()
        
        # Get the project directory path
        # Used by: ProjectController.get_project_path()
        project_path = ProjectController().get_project_path(project_id=project_id)

        # Clean the original file name
        # Used by: self.get_clean_file_name()
        cleaned_file_name = self.get_clean_file_name(
            orig_file_name=orig_file_name
        )

        # Create the new file path
        new_file_path = os.path.join(
            project_path,
            random_key + "_" + cleaned_file_name
        )

        # Ensure uniqueness by regenerating if file already exists
        while os.path.exists(new_file_path):
            random_key = self.generate_random_string()
            new_file_path = os.path.join(
                project_path,
                random_key + "_" + cleaned_file_name
            )

        return new_file_path, random_key + "_" + cleaned_file_name

    def get_clean_file_name(self, orig_file_name: str):
        """
        Clean and sanitize file names for safe storage
        
        This method removes special characters and spaces from file names
        to ensure they are safe for file system storage.
        
        Args:
            orig_file_name (str): Original file name to clean
        
        Returns:
            str: Cleaned file name safe for file system storage
        
        Used by:
            - self.generate_unique_filepath(): For cleaning file names before storage
        """
        # Remove any special characters, except underscore and .
        cleaned_file_name = re.sub(r'[^\w.]', '', orig_file_name.strip())

        # Replace spaces with underscore
        cleaned_file_name = cleaned_file_name.replace(" ", "_")

        return cleaned_file_name