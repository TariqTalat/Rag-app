"""
Database Enum Module
====================

This module defines enumeration constants for MongoDB collection names
used throughout the application. These enums ensure consistent
collection naming across all database operations.

Dependencies:
- enum: For defining enumeration types
"""

# Step 1: Import Enum from the enum module
from enum import Enum

class DataBaseEnum(Enum):
    """
    Defines standard collection names for MongoDB collections.
    """
    # Step 2: Collection for storing project information
    COLLECTION_PROJECT_NAME = "projects"
    # Step 3: Collection for storing processed data chunks
    COLLECTION_CHUNK_NAME = "chunks"
    # Step 4: Collection for storing asset information
    COLLECTION_ASSET_NAME = "assets"
    # Usage example:
    #   DataBaseEnum.COLLECTION_PROJECT_NAME.value -> 'projects'