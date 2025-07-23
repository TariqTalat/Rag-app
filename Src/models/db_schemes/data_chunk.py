"""
Data Chunk Schema Module
========================

Stepwise Breakdown:
-------------------
1. Import Pydantic and typing dependencies.
2. Define the DataChunk Pydantic model for chunk documents.
3. Add field validation and configuration.

This module defines the schema for a data chunk stored in the database.
It uses Pydantic for type validation and serialization.

Dependencies:
- pydantic: For data validation and model definition
- typing: For type hints
- bson.objectid.ObjectId: For MongoDB object IDs
"""

from pydantic import BaseModel, Field, validator
from typing import Optional
from bson.objectid import ObjectId

class DataChunk(BaseModel):
    """
    Data Chunk Schema
    -----------------
    Represents a chunk of text and its metadata for storage in the database.

    Attributes:
        id (Optional[ObjectId]): MongoDB document ID
        chunk_text (str): The text content of the chunk
        chunk_metadata (dict): Metadata associated with the chunk
        chunk_order (int): The order of the chunk in the file
        chunk_project_id (ObjectId): The project this chunk belongs to

    Example usage:
        >>> chunk = DataChunk(chunk_text='abc', chunk_metadata={}, chunk_order=1, chunk_project_id=ObjectId())
        >>> print(chunk.dict())
    """
    # Step 1: MongoDB document ID (optional, uses alias '_id')
    id: Optional[ObjectId] = Field(None, alias="_id")
    # Step 2: The text content of the chunk (must not be empty)
    chunk_text: str = Field(..., min_length=1)
    # Step 3: Metadata dictionary for the chunk
    chunk_metadata: dict
    # Step 4: The order of the chunk in the file (must be > 0)
    chunk_order: int = Field(..., gt=0)
    # Step 5: The project this chunk belongs to
    chunk_project_id: ObjectId
    chunk_asset_id: ObjectId

    class Config:
        arbitrary_types_allowed = True
    
    @classmethod
    def get_indexes(cls):
        """
        Get the indexes for the DataChunk model.

        Returns:
            list: A list of indexes for the DataChunk model
        """
        return [
            {
                "key": [
                    ("chunk_project_id", 1)
                ],
                "name": "chunk_project_id_index_1",
                "unique": False
            }
        ]
    