"""
Main FastAPI Application Entry Point
====================================

Stepwise Breakdown:
-------------------
1. Import FastAPI, routers, and configuration dependencies.
2. Initialize the FastAPI app.
3. Set up MongoDB connection on startup and shutdown events.
4. Include routers for base and data endpoints.

This module serves as the main entry point for the mini-RAG FastAPI application.
It initializes the FastAPI app and includes all the necessary routers for different
API endpoints.

Dependencies:
- FastAPI: Web framework for building APIs
- routes.base: Base router for general API endpoints
- routes.data: Data router for file upload and data management endpoints
- motor.motor_asyncio: MongoDB async driver
- helpers.config: Application settings
"""

from fastapi import FastAPI
from routes import base
from routes import data
from motor.motor_asyncio import AsyncIOMotorClient
from helpers.config import get_settings

# Step 1: Initialize the FastAPI application with default settings
app = FastAPI()

@app.on_event("startup")
async def startup_db_client():
    """
    Startup Event: Initialize MongoDB Connection
    --------------------------------------------
    Creates async MongoDB client and database connection
    using settings from environment variables.

    Example usage:
        This runs automatically when the FastAPI app starts.
    """
    # Step 1: Get application settings for database configuration
    settings = get_settings()
    # Step 2: Create MongoDB async client connection
    app.mongo_conn = AsyncIOMotorClient(settings.MONGODB_URL)
    # Step 3: Set database client for the application
    app.db_client = app.mongo_conn[settings.MONGODB_DATABASE]

@app.on_event("shutdown")
async def shutdown_db_client():
    """
    Shutdown Event: Close MongoDB Connection
    ----------------------------------------
    Ensures proper cleanup of database connections.

    Example usage:
        This runs automatically when the FastAPI app shuts down.
    """
    # Step 1: Close MongoDB connection to free resources
    app.mongo_conn.close()

# Step 2: Include the base router for general API endpoints
# Used by: routes/base.py -> base_router
app.include_router(base.base_router)

# Step 3: Include the data router for file upload and data management endpoints
# Used by: routes/data.py -> data_router
app.include_router(data.data_router)




