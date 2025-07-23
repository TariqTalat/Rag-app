from enum import Enum

class DataBaseEnum(Enum):
    """
    Enum for collection names in the database.
    This enum is used to define the names of collections
    used in the application, ensuring consistency and
    avoiding hard-coded strings throughout the codebase.
    """

    COLLECTION_PROJECT_NAME = "projects"
    COLLECTION_CHUNK_NAME = "chunks"
    COLLECTION_ASSET_NAME = "assets"