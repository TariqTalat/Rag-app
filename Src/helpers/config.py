"""
Configuration Management Module
===============================

This module handles application configuration using Pydantic Settings.
It manages environment variables and provides type-safe configuration
access throughout the application.

Dependencies:
- pydantic_settings: For type-safe configuration management
- .env file: Environment variables file

Used by:
- controllers/BaseController.py: For accessing app settings
- routes/base.py: For dependency injection in API endpoints
- routes/data.py: For dependency injection in file upload endpoints
"""

from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """
    Application Settings Configuration
    
    This class defines all the configuration parameters for the mini-RAG application.
    It uses Pydantic for type validation and automatic environment variable loading.
    
    Attributes:
        APP_NAME (str): Name of the application
        APP_VERSION (str): Version of the application
        OPENAI_API_KEY (str): OpenAI API key for AI operations
        FILE_ALLOWED_TYPES (list[str]): List of allowed file types for upload
        FILE_MAX_SIZE (int): Maximum file size in MB
        FILE_DEFAULT_CHUNK_SIZE (int): Default chunk size for file processing
    """
    APP_NAME: str
    APP_VERSION: str
    OPENAI_API_KEY: str
    FILE_ALLOWED_TYPES: list[str]
    FILE_MAX_SIZE: int
    FILE_DEFAULT_CHUNK_SIZE: int
    
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
    Get the application settings.
    
    This function creates and returns a Settings instance with all configuration
    loaded from environment variables and the .env file.
    
    Returns:
        Settings: An instance of the Settings class containing the application configuration.
    
    Used by:
        - controllers/BaseController.py: For initializing controller settings
        - routes/base.py: As dependency injection for API endpoints
        - routes/data.py: As dependency injection for file upload endpoints
    """
    return Settings()