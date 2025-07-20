"""
Database Enum Module
====================

This module defines enumeration constants for MongoDB collection names
used throughout the application. These enums ensure consistent
collection naming across all database operations.

Used by:
- models/ProjectModel.py: For project collection naming
- models/DataChunkModel.py: For data chunk collection naming
"""

from enum import Enum

class DataBaseEnum(Enum):
    """
    Database Collection Names Enum
    
    Defines standard collection names for MongoDB collections
    to ensure consistency across the application.
    
    Enum Values:
        COLLECTION_PROJECT_NAME: Collection for storing project data
        COLLECTION_CHUNK_NAME: Collection for storing data chunks
    """
    # Collection for storing project information
    COLLECTION_PROJECT_NAME = "projects"
    
    # Collection for storing processed data chunks
    COLLECTION_CHUNK_NAME = "chunks"