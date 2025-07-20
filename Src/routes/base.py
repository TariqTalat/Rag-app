"""
Base Router Module
==================

Stepwise Breakdown:
-------------------
1. Import FastAPI, APIRouter, and dependencies.
2. Create the base_router for general API endpoints.
3. Define the welcome endpoint for application info and health check.

This module defines the base API router that handles general application
endpoints such as health checks and application information. It provides
basic API functionality that doesn't require specific business logic.

Dependencies:
- fastapi: For API router and dependency injection
- os: For environment operations (imported but not used in current version)
- helpers.config: For application settings and dependency injection
"""

from fastapi import FastAPI, APIRouter, Depends
import os
from helpers.config import get_settings, Settings

# Step 1: Create base router with API version prefix and tags
base_router = APIRouter(prefix="/api/v1", tags=["api_v1"])

@base_router.get("/")
async def welcome(app_settings: Settings = Depends(get_settings)):
    """
    Welcome Endpoint
    ----------------
    Provides basic information about the application including the app name and version.
    Serves as a health check and application identification endpoint.

    Args:
        app_settings (Settings): Application settings injected by FastAPI
    Returns:
        dict: Dictionary containing app_name and app_version

    Example usage (with FastAPI TestClient):
        >>> from fastapi.testclient import TestClient
        >>> from main import app
        >>> client = TestClient(app)
        >>> response = client.get('/api/v1/')
        >>> response.json()
        {'app_name': 'MyApp', 'app_version': '1.0.0'}
    """
    # Step 1: Extract application name from settings
    app_name = app_settings.APP_NAME
    # Step 2: Extract application version from settings
    app_version = app_settings.APP_VERSION
    # Step 3: Return application metadata as JSON response
    return {
        "app_name": app_name,
        "app_version": app_version,
    }