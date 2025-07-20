"""
Database Enum Module
====================

Stepwise Breakdown:
-------------------
1. Import Enum from the enum module.
2. Define the DataBaseEnum class for MongoDB collection names.
3. Add enum values for project and chunk collections.

This module defines enumeration constants for MongoDB collection names
used throughout the application. These enums ensure consistent
collection naming across all database operations.

Dependencies:
- enum: For defining enumeration types
"""

from enum import Enum

class DataBaseEnum(Enum):
    """
    Database Collection Names Enum
    -----------------------------
    Defines standard collection names for MongoDB collections
    to ensure consistency across the application.

    Enum Values:
        COLLECTION_PROJECT_NAME: Collection for storing project data
        COLLECTION_CHUNK_NAME: Collection for storing data chunks

    Example usage:
        >>> DataBaseEnum.COLLECTION_PROJECT_NAME.value
        'projects'
    """
    # Step 1: Collection for storing project information
    COLLECTION_PROJECT_NAME = "projects"
    # Step 2: Collection for storing processed data chunks
    COLLECTION_CHUNK_NAME = "chunks"