"""
Base Controller Module
======================

Stepwise Breakdown:
-------------------
1. Import dependencies and configuration helpers.
2. Define the BaseController class for shared controller logic.
3. Initialize application settings and directory paths.
4. Provide utility for generating random strings.

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
    --------------------
    Provides common functionality and utilities for all controllers
    in the application. Handles configuration management, file system setup,
    and provides utility methods for string generation.

    Attributes:
        app_settings (Settings): Application configuration settings
        base_dir (str): Base directory path of the application
        files_dir (str): Directory path for storing uploaded files

    Example usage:
        >>> base = BaseController()
        >>> rand_str = base.generate_random_string(8)
        >>> print(base.files_dir)
    """
    
    def __init__(self):
        """
        Initialize the base controller with application settings and directory paths.
        Sets up the controller with:
        - Application settings from the configuration
        - Base directory path for the application
        - Files directory path for storing uploaded files

        Example usage:
            >>> base = BaseController()
            >>> print(base.app_settings.APP_NAME)
        """
        # Step 1: Load application settings from configuration
        self.app_settings = get_settings()
        # Step 2: Set up base directory path (two levels up from controllers directory)
        self.base_dir = os.path.dirname(os.path.dirname(__file__))
        # Step 3: Set up files directory path for storing uploaded files
        self.files_dir = os.path.join(self.base_dir, "assets/files")
    
    def generate_random_string(self, length: int=12):
        """
        Generate a random string of specified length.
        Creates random strings using lowercase letters and digits. Used for unique file names and identifiers.

        Args:
            length (int): Length of the random string to generate (default: 12)
        Returns:
            str: Random string containing lowercase letters and digits

        Example usage:
            >>> BaseController().generate_random_string(6)
            'a1b2c3'
        """
        # Step 1: Generate random string using lowercase letters and digits
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))