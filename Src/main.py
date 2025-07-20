"""
Main FastAPI Application Entry Point
====================================

This module serves as the main entry point for the mini-RAG FastAPI application.
It initializes the FastAPI app and includes all the necessary routers for different
API endpoints.

Dependencies:
- FastAPI: Web framework for building APIs
- routes.base: Base router for general API endpoints
- routes.data: Data router for file upload and data management endpoints
- motor.motor_asyncio: MongoDB async driver
- helpers.config: Application settings

Router Connections:
- base_router: Handles general API endpoints (health check, app info)
- data_router: Handles file upload and data processing endpoints
"""

from fastapi import FastAPI
from routes import base
from routes import data
from motor.motor_asyncio import AsyncIOMotorClient
from helpers.config import get_settings


# Initialize the FastAPI application with default settings
app = FastAPI()

@app.on_event("startup")
async def startup_db_client():
    """
    Initialize MongoDB connection on app startup
    
    Creates async MongoDB client and database connection
    using settings from environment variables
    """
    # Get application settings for database configuration
    settings = get_settings()
    
    # Create MongoDB async client connection
    app.mongo_conn = AsyncIOMotorClient(settings.MONGODB_URL)
    
    # Set database client for the application
    app.db_client = app.mongo_conn[settings.MONGODB_DATABASE]

@app.on_event("shutdown")
async def shutdown_db_client():
    """
    Close MongoDB connection on app shutdown
    
    Ensures proper cleanup of database connections
    """
    # Close MongoDB connection to free resources
    app.mongo_conn.close()

# Include the base router for general API endpoints
# Used by: routes/base.py -> base_router
app.include_router(base.base_router)

# Include the data router for file upload and data management endpoints
# Used by: routes/data.py -> data_router
app.include_router(data.data_router)




