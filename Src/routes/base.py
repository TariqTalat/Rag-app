"""
Base Router Module
==================

This module defines the base API router that handles general application
endpoints such as health checks and application information. It provides
basic API functionality that doesn't require specific business logic.

Dependencies:
- fastapi: For API router and dependency injection
- os: For environment operations (imported but not used in current version)
- helpers.config: For application settings and dependency injection

Used by:
- main.py: Included in the main FastAPI application
"""

from fastapi import FastAPI, APIRouter, Depends
import os
from helpers.config import get_settings, Settings

# Create base router with API version prefix and tags
base_router = APIRouter(prefix="/api/v1", tags=["api_v1"])

@base_router.get("/")
async def welcome(app_settings: Settings = Depends(get_settings)):
    """
    Welcome endpoint for application information
    
    This endpoint provides basic information about the application
    including the app name and version. It serves as a health check
    and application identification endpoint.
    
    Args:
        app_settings (Settings): Application settings injected by FastAPI
    
    Returns:
        dict: Dictionary containing app_name and app_version
    
    Used by:
        - main.py: Included in the base_router for general API access
        - External clients: For application identification and health checks
    
    Dependencies:
        - helpers/config.py -> get_settings(): For dependency injection
        - helpers/config.py -> Settings: For type hints and configuration access
    """
    # Extract application name from settings
    # Used by: helpers/config.py -> Settings.APP_NAME
    app_name = app_settings.APP_NAME
    
    # Extract application version from settings
    # Used by: helpers/config.py -> Settings.APP_VERSION
    app_version = app_settings.APP_VERSION

    return {
        "app_name": app_name,
        "app_version": app_version,
    }