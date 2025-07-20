"""
Base Data Model Module
======================

Stepwise Breakdown:
-------------------
1. Import configuration helpers.
2. Define the BaseDataModel class for shared database logic.
3. Initialize with a database client and application settings.

This module provides a base class for all data models that interact with the database.
It stores the database client and application settings for use in subclasses.

Dependencies:
- helpers.config: For application settings management
"""

from helpers.config import get_settings, Settings

class BaseDataModel:
    """
    Base Data Model Class
    ---------------------
    Provides shared logic for all data models, including access to the database client
    and application settings.

    Attributes:
        db_client (object): MongoDB client instance
        app_settings (Settings): Application configuration settings

    Example usage:
        >>> base = BaseDataModel(db_client)
        >>> print(base.app_settings.APP_NAME)
    """

    def __init__(self, db_client: object):
        """
        Initialize the base data model with a database client and app settings.

        Args:
            db_client (object): MongoDB client instance

        Example usage:
            >>> base = BaseDataModel(db_client)
        """
        # Step 1: Store the database client
        self.db_client = db_client
        # Step 2: Load application settings
        self.app_settings = get_settings()