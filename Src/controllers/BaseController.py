"""
Base Controller Module
======================

This module provides the base controller class that contains common functionality
and utilities used by all other controllers in the application. It handles
configuration management, file system operations, and utility functions.

Dependencies:
- helpers.config: For application settings management
- os: For file system operations
- random, string: For generating random strings

Used by:
- controllers/DataController.py: Inherits from BaseController
- controllers/ProjectController.py: Inherits from BaseController
"""

from helpers.config import get_settings, Settings
import os
import random
import string

class BaseController:
    """
    Base Controller Class
    
    This class provides common functionality and utilities for all controllers
    in the application. It handles configuration management, file system setup,
    and provides utility methods for string generation.
    
    Attributes:
        app_settings (Settings): Application configuration settings
        base_dir (str): Base directory path of the application
        files_dir (str): Directory path for storing uploaded files
    
    Used by:
        - DataController: For file validation and processing operations
        - ProjectController: For project directory management
    """
    
    def __init__(self):
        """
        Initialize the base controller with application settings and directory paths
        
        This method sets up the controller with:
        - Application settings from the configuration
        - Base directory path for the application
        - Files directory path for storing uploaded files
        """
        # Load application settings from configuration
        # Used by: helpers/config.py -> get_settings()
        self.app_settings = get_settings()
        
        # Set up base directory path (two levels up from controllers directory)
        self.base_dir = os.path.dirname( os.path.dirname(__file__) )
        
        # Set up files directory path for storing uploaded files
        self.files_dir = os.path.join(
            self.base_dir,
            "assets/files"
        )
        
    def generate_random_string(self, length: int=12):
        """
        Generate a random string of specified length
        
        This utility method creates random strings using lowercase letters
        and digits. It's used for generating unique file names and identifiers.
        
        Args:
            length (int): Length of the random string to generate (default: 12)
        
        Returns:
            str: Random string containing lowercase letters and digits
        
        Used by:
            - DataController.generate_unique_filepath(): For creating unique file names
        """
        # Generate random string using lowercase letters and digits
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))