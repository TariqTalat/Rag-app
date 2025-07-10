'''
This module defines the applications configuration settings using Pydantic.
It uses environment variables to set the configuration values.
This allows for easy management of application settings and ensures that
the application can be configured without changing the codebase.
It also provides a function to retrieve the settings instance.
This is useful for accessing configuration values throughout the application.
'''
from pydantic_settings import BaseSettings, SettingsConfigDict # This library is used for managing application settings
# SETTINGSConfigDict is used to define the configuration for the settings class
# BaseSettings is the base class for creating settings classes with Pydantic
class Settings(BaseSettings):
    APP_NAME: str
    APP_VERSION: str
    OPENAI_API_KEY: str
    FILE_ALLOWED_TYPES: list[str]
    FILE_MAX_SIZE: int
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True
        extra = "forbid"

def get_settings() -> Settings:
    """
    Get the application settings.
    
    Returns:
        Settings: An instance of the Settings class containing the application configuration.
    """
    return Settings()