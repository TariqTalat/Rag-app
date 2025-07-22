"""
Project Schema Module
=====================

Stepwise Breakdown:
-------------------
1. Import Pydantic and typing dependencies.
2. Define the Project Pydantic model for project documents.
3. Add field validation and configuration.

This module defines the schema for a project stored in the database.
It uses Pydantic for type validation and serialization.

Dependencies:
- pydantic: For data validation and model definition
- typing: For type hints
- bson.objectid.ObjectId: For MongoDB object IDs
"""

from pydantic import BaseModel, Field, validator
from typing import Optional
from bson.objectid import ObjectId

class Project(BaseModel):
    """
    Project Schema
    --------------
    Represents a project document for storage in the database.

    Attributes:
        id (Optional[ObjectId]): MongoDB document ID
        project_id (str): The unique project identifier (alphanumeric)

    Example usage:
        >>> project = Project(project_id='proj1')
        >>> print(project.dict())
    """
    # Step 1: MongoDB document ID (optional, uses alias '_id')
    id: Optional[ObjectId] = Field(None, alias="_id")
    # Step 2: The unique project identifier (must be alphanumeric)
    project_id: str = Field(..., min_length=1)

    @validator('project_id')
    def validate_project_id(cls, value):
        """
        Validate that the project_id is alphanumeric.

        Args:
            value (str): The project_id to validate
        Returns:
            str: The validated project_id
        Raises:
            ValueError: If project_id is not alphanumeric

        Example usage:
            >>> Project.validate_project_id('proj1')
        """
        # Step 1: Ensure project_id is alphanumeric
        if not value.isalnum():
            raise ValueError('project_id must be alphanumeric')
        # Step 2: Return the validated value
        return value

    class Config:
        arbitrary_types_allowed = True
    
    @classmethod
    def get_indexes(cls):
        """
        Get the indexes for the Project model.

        Returns:
            list: A list of indexes for the Project model
        """
        return [
            {
                "key": [
                    ("project_id", 1)
                ],
                "name": "project_id_index_1",
                "unique": True
            }
        ]