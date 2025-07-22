"""
Chunk Model Module
==================

Stepwise Breakdown:
-------------------
1. Import dependencies and base data model.
2. Define the ChunkModel class for chunk database operations.
3. Implement methods for creating, retrieving, inserting, and deleting chunks.

This module provides the data model for handling chunk records in the database.
It supports creating, retrieving, batch inserting, and deleting chunk documents.

Dependencies:
- .BaseDataModel: Base class for MongoDB operations
- .db_schemes.DataChunk: Pydantic model for chunk schema
- .enums.DataBaseEnum: Enum for collection names
- bson.objectid.ObjectId: For MongoDB object IDs
- pymongo.InsertOne: For batch insert operations
"""

from .BaseDataModel import BaseDataModel
from .db_schemes import DataChunk
from .enums.DataBaseEnum import DataBaseEnum
from bson.objectid import ObjectId
from pymongo import InsertOne

class ChunkModel(BaseDataModel):
    """
    Chunk Model Class
    -----------------
    Handles database operations for data chunks, including creation,
    retrieval, batch insertion, and deletion by project.

    Example usage:
        >>> cm = ChunkModel(db_client)
        >>> chunk = DataChunk(chunk_text='abc', chunk_metadata={}, chunk_order=1, chunk_project_id=ObjectId())
        >>> created = await cm.create_chunk(chunk)
        >>> fetched = await cm.get_chunk(str(created.id))
    """

    def __init__(self, db_client: object):
        """
        Initialize the chunk model with a database client.

        Args:
            db_client (object): MongoDB client instance

        Example usage:
            >>> cm = ChunkModel(db_client)
        """
        # Step 1: Initialize base data model
        super().__init__(db_client=db_client)
        # Step 2: Set collection for chunks
        self.collection = self.db_client[DataBaseEnum.COLLECTION_CHUNK_NAME.value]

    @classmethod
    async def create_instance(cls,db_client: object):
        instance = cls(db_client=db_client)
        await instance.init_collection()
        return instance
    
    async def init_collection(self):
        all_collections = await self.db_client.list_collection_names()
        if DataBaseEnum.COLLECTION_CHUNK_NAME.value not in all_collections:
            self.collection = self.db_client[DataBaseEnum.COLLECTION_CHUNK_NAME.value]
            indexes = DataChunk.get_indexes()
            for index in indexes:
                await self.collection.create_index(index['key'],
                                                   name=index['name'],
                                                   unique=index["unique"])

    async def create_chunk(self, chunk: DataChunk):
        """
        Create a new chunk document in the database.

        Args:
            chunk (DataChunk): The chunk data to insert
        Returns:
            DataChunk: The inserted chunk with its MongoDB ID

        Example usage:
            >>> created = await cm.create_chunk(chunk)
        """
        # Step 1: Insert chunk document
        result = await self.collection.insert_one(chunk.dict(by_alias=True, exclude_unset=True))
        # Step 2: Assign inserted ID to chunk
        chunk._id = result.inserted_id
        # Step 3: Return the chunk
        return chunk

    async def get_chunk(self, chunk_id: str):
        """
        Retrieve a chunk document by its ID.

        Args:
            chunk_id (str): The MongoDB ObjectId as a string
        Returns:
            DataChunk or None: The chunk if found, else None

        Example usage:
            >>> chunk = await cm.get_chunk('60f...')
        """
        # Step 1: Query for chunk by ObjectId
        result = await self.collection.find_one({"_id": ObjectId(chunk_id)})
        # Step 2: Return None if not found
        if result is None:
            return None
        # Step 3: Return DataChunk instance
        return DataChunk(**result)

    async def insert_many_chunks(self, chunks: list, batch_size: int=100):
        """
        Insert multiple chunk documents in batches.

        Args:
            chunks (list): List of DataChunk objects
            batch_size (int): Number of chunks per batch (default: 100)
        Returns:
            int: Total number of inserted chunks

        Example usage:
            >>> n = await cm.insert_many_chunks([chunk1, chunk2])
        """
        # Step 1: Insert chunks in batches
        for i in range(0, len(chunks), batch_size):
            batch = chunks[i:i+batch_size]
            # Step 2: Prepare insert operations
            operations = [InsertOne(chunk.dict(by_alias=True, exclude_unset=True)) for chunk in batch]
            # Step 3: Execute batch insert
            await self.collection.bulk_write(operations)
        # Step 4: Return total inserted
        return len(chunks)

    async def delete_chunks_by_project_id(self, project_id: ObjectId):
        """
        Delete all chunks associated with a specific project.

        Args:
            project_id (ObjectId): The project identifier
        Returns:
            int: Number of deleted chunk documents

        Example usage:
            >>> deleted = await cm.delete_chunks_by_project_id(ObjectId('60f...'))
        """
        # Step 1: Delete all chunks with matching project_id
        result = await self.collection.delete_many({"chunk_project_id": project_id})
        # Step 2: Return number of deleted documents
        return result.deleted_count