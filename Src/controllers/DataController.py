"""
Data Controller Module
======================

Stepwise Breakdown:
-------------------
1. Import dependencies and base classes.
2. Define the DataController class for file validation and upload logic.
3. Implement file validation (type and size).
4. Implement unique file path generation for uploads.
5. Implement file name cleaning for safe storage.

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
    --------------------
    Handles all data processing operations including file validation,
    file upload management, and file path generation. Inherits from BaseController.

    Attributes:
        size_scale (int): Conversion factor from MB to bytes (1048576)

    Example usage:
        >>> controller = DataController()
        >>> is_valid, msg = controller.validate_uploaded_file(file)
        >>> path, fname = controller.generate_unique_filepath('my.txt', 'proj1')
    """
    
    def __init__(self):
        """
        Initialize the data controller with size conversion settings.
        Sets up the controller with a size scale factor for converting
        between MB and bytes for file size validation.

        Example usage:
            >>> controller = DataController()
        """
        # Step 1: Initialize parent class (BaseController)
        super().__init__()
        # Step 2: Set size scale factor: 1 MB = 1048576 bytes
        self.size_scale = 1048576 # convert MB to bytes

    def validate_uploaded_file(self, file: UploadFile):
        """
        Validate uploaded file for type and size compliance.
        Checks if the uploaded file meets the application's requirements for file type and size limits.

        Args:
            file (UploadFile): The uploaded file to validate
        Returns:
            tuple: (bool, str) - (is_valid, response_message)

        Example usage:
            >>> is_valid, msg = DataController().validate_uploaded_file(file)
        """
        # Step 1: Check if file type is in the allowed types list
        if file.content_type not in self.app_settings.FILE_ALLOWED_TYPES:
            return False, ResponseSignals.FILE_TYPE_NOT_SUPPORTED.value
        # Step 2: Check if file size exceeds the maximum allowed size
        if file.size > self.app_settings.FILE_MAX_SIZE * self.size_scale:
            return False, ResponseSignals.FILE_SIZE_EXCEEDED.value
        # Step 3: File is valid
        return True, ResponseSignals.FILE_VALIDATE_SUCCESS.value

    def generate_unique_filepath(self, orig_file_name: str, project_id: str):
        """
        Generate a unique file path for uploaded files.
        Creates a unique file path by combining a random string with the cleaned original file name.

        Args:
            orig_file_name (str): Original name of the uploaded file
            project_id (str): ID of the project for directory organization
        Returns:
            tuple: (str, str) - (full_file_path, unique_file_name)

        Example usage:
            >>> path, fname = DataController().generate_unique_filepath('my.txt', 'proj1')
        """
        # Step 1: Generate a random key for uniqueness
        random_key = self.generate_random_string()
        # Step 2: Get the project directory path
        project_path = ProjectController().get_project_path(project_id=project_id)
        # Step 3: Clean the original file name
        cleaned_file_name = self.get_clean_file_name(orig_file_name=orig_file_name)
        # Step 4: Create the new file path with random prefix
        new_file_path = os.path.join(project_path, random_key + "_" + cleaned_file_name)
        # Step 5: Ensure uniqueness by regenerating if file already exists
        while os.path.exists(new_file_path):
            random_key = self.generate_random_string()
            new_file_path = os.path.join(project_path, random_key + "_" + cleaned_file_name)
        # Step 6: Return the unique file path and name
        return new_file_path, random_key + "_" + cleaned_file_name

    def get_clean_file_name(self, orig_file_name: str):
        """
        Clean and sanitize file names for safe storage.
        Removes special characters and spaces from file names to ensure they are safe for file system storage.

        Args:
            orig_file_name (str): Original file name to clean
        Returns:
            str: Cleaned file name safe for file system storage

        Example usage:
            >>> DataController().get_clean_file_name('my file@2024.txt')
            'myfile2024.txt'
        """
        # Step 1: Remove any special characters, except underscore and dot
        cleaned_file_name = re.sub(r'[^\w.]', '', orig_file_name.strip())
        # Step 2: Replace spaces with underscore for better file system compatibility
        cleaned_file_name = cleaned_file_name.replace(" ", "_")
        # Step 3: Return cleaned name
        return cleaned_file_name