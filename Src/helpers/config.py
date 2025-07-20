"""
Configuration Management Module
===============================

Stepwise Breakdown:
-------------------
1. Import Pydantic settings dependencies.
2. Define the Settings class for application configuration.
3. Implement the get_settings function for loading settings.

This module handles application configuration using Pydantic Settings.
It manages environment variables and provides type-safe configuration
access throughout the application.

Dependencies:
- pydantic_settings: For type-safe configuration management
- .env file: Environment variables file
"""

from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """
    Application Settings Configuration
    ----------------------------------
    Defines all the configuration parameters for the mini-RAG application.
    Uses Pydantic for type validation and automatic environment variable loading.

    Attributes:
        APP_NAME (str): Name of the application
        APP_VERSION (str): Version of the application
        OPENAI_API_KEY (str): OpenAI API key for AI operations
        FILE_ALLOWED_TYPES (list[str]): List of allowed file types for upload
        FILE_MAX_SIZE (int): Maximum file size in MB
        FILE_DEFAULT_CHUNK_SIZE (int): Default chunk size for file processing
        MONGODB_URL (str): MongoDB connection string
        MONGODB_DATABASE (str): MongoDB database name

    Example usage:
        >>> settings = Settings()
        >>> print(settings.APP_NAME)
    """
    # Step 1: Application metadata
    APP_NAME: str
    APP_VERSION: str
    # Step 2: API configuration
    OPENAI_API_KEY: str
    # Step 3: File upload settings
    FILE_ALLOWED_TYPES: list[str]
    FILE_MAX_SIZE: int
    FILE_DEFAULT_CHUNK_SIZE: int
    # Step 4: Database configuration
    MONGODB_URL: str
    MONGODB_DATABASE: str

    class Config:
        """
        Pydantic configuration for environment variable loading
        """
        env_file = ".env"  # Load from .env file
        env_file_encoding = "utf-8"  # File encoding
        case_sensitive = True  # Case sensitive field names
        extra = "forbid"  # Forbid extra fields not defined in the model


def get_settings() -> Settings:
    """
    Get Application Settings
    ------------------------
    Creates and returns a Settings instance with all configuration
    loaded from environment variables and the .env file.

    Returns:
        Settings: An instance of the Settings class containing the application configuration.

    Example usage:
        >>> settings = get_settings()
        >>> print(settings.MONGODB_URL)
    """
    # Step 1: Create and return Settings instance with environment variables
    return Settings()