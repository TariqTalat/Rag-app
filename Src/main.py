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

Router Connections:
- base_router: Handles general API endpoints (health check, app info)
- data_router: Handles file upload and data processing endpoints
"""

from fastapi import FastAPI
from routes import base
from routes import data

# Initialize the FastAPI application
app = FastAPI()

# Include the base router for general API endpoints
# Used by: routes/base.py -> base_router
app.include_router(base.base_router)

# Include the data router for file upload and data management endpoints
# Used by: routes/data.py -> data_router
app.include_router(data.data_router)


