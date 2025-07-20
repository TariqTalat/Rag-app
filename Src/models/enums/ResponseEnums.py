"""
Response Signal Enums
=====================

Stepwise Breakdown:
-------------------
1. Import Enum from the enum module.
2. Define the ResponseSignals class for standardized response messages.
3. Add enum values for all possible API response signals.

This module defines enumeration constants for standardized response signals
used throughout the application. These enums ensure consistent error handling
and response messaging across all API endpoints.

Dependencies:
- enum: For defining enumeration types
"""

from enum import Enum

class ResponseSignals(Enum):
    """
    Standardized Response Signals Enum
    ---------------------------------
    Defines all possible response signals that can be returned
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
        FILE_PROCESSING_FAIL: File processing failed
        FILE_PROCESSING_SUCCESS: File processing successful

    Example usage:
        >>> ResponseSignals.FILE_UPLOAD_SUCCESS.value
        'file uploaded successfully'
    """
    # Step 1: File validation responses
    FILE_VALIDATE_SUCCESS = "file validation successful"
    FILE_VALIDATE_FAIL = "file validation failed"
    # Step 2: File operation responses
    FILE_NOT_FOUND = "file not found"
    FILE_TYPE_NOT_SUPPORTED = "file type not supported"
    FILE_SIZE_EXCEEDED = "file size exceeded"
    # Step 3: File upload responses
    FILE_UPLOAD_SUCCESS = "file uploaded successfully"
    FILE_UPLOADED_FAIL = "file upload failed"
    # Step 4: File processing responses
    FILE_PROCESSING_FAIL = "file processing failed"
    FILE_PROCESSING_SUCCESS = "file processing successful"