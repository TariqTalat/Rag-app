"""
Configuration Module
====================

This module defines the application settings using Pydantic's BaseSettings.
It loads environment variables and provides structured access to configuration values.

Dependencies:
- pydantic_settings: For environment-based settings management
"""

# Import BaseSettings for configuration management
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """
    Defines the structure for application settings.

    Attributes:
    - APP_NAME: Name of the application
    - APP_VERSION: Version of the application
    - OPENAI_API_KEY: API key for OpenAI
    - FILE_ALLOWED_TYPES: Allowed file types for upload
    - FILE_MAX_SIZE: Maximum file size for upload
    - FILE_DEFAULT_CHUNK_SIZE: Default chunk size for file processing
    - MONGODB_URL: MongoDB connection URL
    - MONGODB_DATABASE: MongoDB database name
    - GENERATION_BACKEND: Backend for text generation
    - EMBEDDING_BACKEND: Backend for embeddings
    - GENERATION_MODEL_ID: Model ID for generation tasks
    - EMBEDDING_MODEL_ID: Model ID for embedding tasks
    - EMBEDDING_MODEL_SIZE: Size of embedding vectors
    - INPUT_DAFAULT_MAX_CHARACTERS: Default maximum input characters
    - GENERATION_DAFAULT_MAX_TOKENS: Default maximum tokens for generation
    - GENERATION_DAFAULT_TEMPERATURE: Default temperature for generation
    """

    APP_NAME: str
    APP_VERSION: str
    OPENAI_API_KEY: str

    FILE_ALLOWED_TYPES: list
    FILE_MAX_SIZE: int
    FILE_DEFAULT_CHUNK_SIZE: int

    MONGODB_URL: str
    MONGODB_DATABASE: str

    GENERATION_BACKEND: str
    EMBEDDING_BACKEND: str

    OPENAI_API_KEY: str = None
    OPENAI_API_URL: str = None
    COHERE_API_KEY: str = None

    GENERATION_MODEL_ID: str = None
    EMBEDDING_MODEL_ID: str = None
    EMBEDDING_MODEL_SIZE: int = None
    INPUT_DAFAULT_MAX_CHARACTERS: int = None
    GENERATION_DAFAULT_MAX_TOKENS: int = None
    GENERATION_DAFAULT_TEMPERATURE: float = None

    VECTOR_DB_BACKEND: str
    VECTOR_DB_PATH: str
    VECTOR_DB_DISTANCE_METHOD : str = None

    class Config:
        """
        Configuration class for Pydantic settings.

        Attributes:
        - env_file: Path to the environment file
        """
        env_file = ".env"

# Function to retrieve application settings

def get_settings():
    """
    Returns an instance of the Settings class with loaded environment variables.
    """
    return Settings()