"""
Main Application Module
=======================

This module initializes the FastAPI application, sets up database connections,
and configures LLM providers for generation and embedding tasks.

Dependencies:
- fastapi: For building the web application
- motor: For MongoDB asynchronous client
- helpers.config: For application settings
- stores.llm.LLMProviderFactory: For LLM provider management
"""

# Import FastAPI for web application
from fastapi import FastAPI
# Import routes for base and data endpoints
from routes import base, data
# Import MongoDB asynchronous client
from motor.motor_asyncio import AsyncIOMotorClient
# Import settings helper
from helpers.config import get_settings
# Import LLM provider factory
from stores.llm.LLMProviderFactory import LLMProviderFactory

# Initialize FastAPI application
app = FastAPI()

async def startup_db_client():
    """
    Startup function to initialize database and LLM clients.
    
    Steps:
    1. Retrieve application settings.
    2. Connect to MongoDB.
    3. Initialize LLM provider factory.
    4. Configure generation and embedding clients.
    """
    settings = get_settings()
    app.mongo_conn = AsyncIOMotorClient(settings.MONGODB_URL)
    app.db_client = app.mongo_conn[settings.MONGODB_DATABASE]

    llm_provider_factory = LLMProviderFactory(settings)

    # Step 3: Initialize generation client
    app.generation_client = llm_provider_factory.create(provider=settings.GENERATION_BACKEND)
    app.generation_client.set_generation_model(model_id = settings.GENERATION_MODEL_ID)

    # Step 4: Initialize embedding client
    app.embedding_client = llm_provider_factory.create(provider=settings.EMBEDDING_BACKEND)
    app.embedding_client.set_embedding_model(model_id=settings.EMBEDDING_MODEL_ID,
                                             embedding_size=settings.EMBEDDING_MODEL_SIZE)

async def shutdown_db_client():
    """
    Shutdown function to close database connections.
    """
    app.mongo_conn.close()

# Register startup and shutdown functions
app.router.lifespan.on_startup.append(startup_db_client)
app.router.lifespan.on_shutdown.append(shutdown_db_client)

# Include application routes
app.include_router(base.base_router)
app.include_router(data.data_router)