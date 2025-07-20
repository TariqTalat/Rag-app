"""
Project Controller Module
=========================

Stepwise Breakdown:
-------------------
1. Import dependencies and base classes.
2. Define the ProjectController class for project directory management.
3. Initialize controller with shared logic.
4. Implement method to get or create project directory path.

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
    -----------------------
    Handles project-specific operations including directory creation
    and management. Inherits from BaseController.

    Example usage:
        >>> pc = ProjectController()
        >>> path = pc.get_project_path('proj1')
        >>> print(path)
    """
    
    def __init__(self):
        """
        Initialize the project controller.
        Calls the parent class constructor to inherit common functionality.

        Example usage:
            >>> pc = ProjectController()
        """
        # Step 1: Initialize parent class (BaseController)
        super().__init__()

    def get_project_path(self, project_id: str):
        """
        Get or create project directory path.
        Ensures that a project-specific directory exists for storing uploaded files.
        If the directory doesn't exist, it creates it automatically.

        Args:
            project_id (str): Unique identifier for the project
        Returns:
            str: Full path to the project directory

        Example usage:
            >>> pc = ProjectController()
            >>> path = pc.get_project_path('proj1')
        """
        # Step 1: Create project-specific directory path within the files directory
        project_dir = os.path.join(self.files_dir, project_id)
        # Step 2: Create the project directory if it doesn't exist
        if not os.path.exists(project_dir):
            os.makedirs(project_dir)
        # Step 3: Return the project directory path
        return project_dir