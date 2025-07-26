"""
Project Schema Module
=====================

This module defines the schema for a project stored in the database.
It uses Pydantic for type validation and serialization.

Dependencies:
- pydantic: For data validation and model definition
- typing: For type hints
- bson.objectid.ObjectId: For MongoDB object IDs
"""

# Step 1: Import Pydantic and typing dependencies
from pydantic import BaseModel, Field, validator
from typing import Optional
from bson.objectid import ObjectId

class Project(BaseModel):
    """
    Represents a project document for storage in the database.
    """
    # Step 2: MongoDB document ID (optional, uses alias '_id')
    id: Optional[ObjectId] = Field(None, alias="_id")
    # Step 3: The unique project identifier (must be alphanumeric)
    project_id: str = Field(..., min_length=1)

    @validator('project_id')
    def validate_project_id(cls, value):
        """
        Validate that the project_id is alphanumeric.
        """
        # Step 4: Ensure project_id is alphanumeric
        if not value.isalnum():
            raise ValueError('project_id must be alphanumeric')
        # Step 5: Return the validated value
        return value

    class Config:
        # Step 6: Allow ObjectId type for MongoDB document IDs
        arbitrary_types_allowed = True
    
    @classmethod
    def get_indexes(cls):
        """
        Get the indexes for the Project model.
        """
        # Step 7: Return a list of indexes for the Project model
        return [
            {
                "key": [
                    ("project_id", 1)
                ],
                "name": "project_id_index_1",
                "unique": True
            }
        ]