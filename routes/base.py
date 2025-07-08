from fastapi import FastAPI, APIRouter
import os
base_router = APIRouter() # Create a new router instance

@base_router.get("/") # Define a route for the root path
def welcome_message():
    app_name = os.getenv("APP_NAME")
    app_version = os.getenv("APP_VERSION")
    return {"App Name": app_name,
     "App Version": app_version,
      "message": "Welcome to the FastAPI application!"}