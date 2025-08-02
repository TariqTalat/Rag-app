from abc import ABC, abstractmethod
from typing import List
class VectorDBInterface(ABC):

    @abstractmethod
    def connect(self):
        """Connect to the vector database."""
        pass

    @abstractmethod
    def disconnect(self):
        """Disconnect from the vector database."""
        pass

    @abstractmethod
    def is_collection_existed(self, collection_name: str) -> bool:
        """Check if a collection exists in the vector database."""
        pass

    @abstractmethod
    def list_all_collections(self) -> List:
        """List all collections in the vector database."""
        pass

    @abstractmethod
    def get_collection_info(self, collection_name: str) -> dict: 
        """Get information about a specific collection."""
        pass

    @abstractmethod
    def delete_collection(self, collection_name: str):
        """Delete a specific collection."""
        pass

    @abstractmethod
    def create_collection(self, collection_name: str, embedding_size: int, do_reset: bool = False):
        pass

    @abstractmethod 
    def insert_one(collection_name: str, text: str, vector: list, metadata: dict= None, 
                   record_id: str= None):
        pass

    @abstractmethod
    def insert_many(self, collection_name: str, texts: list, vectors: list,
                    metadata: list = None, record_ids: list = None, batch_size: int = 50):
        """Insert multiple records into a collection."""
        pass  

    @abstractmethod
    def search_by_vector(self, collection_name: str, vector: list, limit: int):
        pass 

