"""
Project Controller Module
=========================

This module handles project-related operations including project directory
management and file organization. It provides functionality for creating
and managing project-specific directories for file storage.

Dependencies:
- .BaseController: Inherits from BaseController for common functionality
- fastapi.UploadFile: For handling file uploads (imported but not used in current version)
- models.ResponseSignals: For standardized response messages (imported but not used in current version)
- os: For file system operations

Used by:
- controllers/DataController.py: For getting project directory paths
- routes/data.py: For project directory management during file uploads
"""

from .BaseController import BaseController
from fastapi import UploadFile
from models import ResponseSignals
import os

class ProjectController(BaseController):
    """
    Project Controller Class
    
    This class handles project-specific operations including directory creation
    and management. It extends BaseController to inherit common functionality
    while providing specialized project handling capabilities.
    
    Used by:
        - DataController: For getting project directory paths during file uploads
        - routes/data.py: For project directory management
    """
    
    def __init__(self):
        """
        Initialize the project controller
        
        Sets up the controller by calling the parent class constructor
        to inherit common functionality from BaseController.
        """
        # Initialize parent class (BaseController)
        super().__init__()

    def get_project_path(self, project_id: str):
        """
        Get or create project directory path
        
        This method ensures that a project-specific directory exists
        for storing uploaded files. If the directory doesn't exist,
        it creates it automatically.
        
        Args:
            project_id (str): Unique identifier for the project
        
        Returns:
            str: Full path to the project directory
        
        Used by:
            - DataController.generate_unique_filepath(): For creating file paths within projects
            - routes/data.py: For project directory management during file uploads
        
        Dependencies:
            - self.files_dir: Base files directory from BaseController
        """
        # Create project-specific directory path within the files directory
        project_dir = os.path.join(
            self.files_dir,  # Base files directory from BaseController
            project_id
        )

        # Create the project directory if it doesn't exist
        if not os.path.exists(project_dir):
            os.makedirs(project_dir)

        return project_dir