"""
Response Signal Enums
====================

This module defines enumeration constants for standardized response signals
used throughout the application. These enums ensure consistent error handling
and response messaging across all API endpoints.

Used by:
- controllers/DataController.py: For file validation responses
- controllers/ProjectController.py: For project operation responses
- routes/data.py: For API response messages
"""

from enum import Enum

class ResponseSignals(Enum):
    """
    Standardized response signals for consistent API responses
    
    This enum defines all possible response signals that can be returned
    by the application's controllers and routes. These signals provide
    consistent messaging for success and error scenarios.
    
    Enum Values:
        FILE_VALIDATE_SUCCESS: File validation completed successfully
        FILE_VALIDATE_FAIL: File validation failed
        FILE_NOT_FOUND: Requested file was not found
        FILE_TYPE_NOT_SUPPORTED: File type is not supported for upload
        FILE_SIZE_EXCEEDED: File size exceeds the maximum allowed limit
        FILE_UPLOAD_SUCCESS: File upload completed successfully
        FILE_UPLOADED_FAIL: File upload failed
    """
    FILE_VALIDATE_SUCCESS = "file validation successful"
    FILE_VALIDATE_FAIL = "file validation failed"
    FILE_NOT_FOUND = "file not found"
    FILE_TYPE_NOT_SUPPORTED = "file type not supported"
    FILE_SIZE_EXCEEDED = "file size exceeded"
    FILE_UPLOAD_SUCCESS = "file uploaded successfully"
    FILE_UPLOADED_FAIL = "file upload failed"
    FILE_PROCESSING_FAIL = "file processing failed"
    FILE_PROCESSING_SUCCESS = "file processing successful"