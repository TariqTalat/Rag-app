"""
Data Request Schema
===================

This module defines the Pydantic model for data processing request
validation. It provides structured input validation for file processing
operations including chunking parameters.

Dependencies:
- pydantic: For data validation and model definition
- typing: For type hints

Used by:
- routes/data.py: For request validation in processing endpoints
"""

from pydantic import BaseModel
from typing import Optional

class ProcessRequest(BaseModel):
    """
    Process Request Schema
    
    Defines the structure and validation rules for file processing
    requests. Includes parameters for chunking configuration and
    processing options.
    
    Attributes:
        file_id (str): Identifier of the file to process
        chunk_size (Optional[int]): Size of text chunks (default: 100)
        overlap_size (Optional[int]): Overlap between chunks (default: 20)
        do_reset (Optional[int]): Reset processing flag (default: 0)
    
    Used by:
        - routes/data.py: For validating processing requests
    """
    # File identifier for processing
    file_id: str
    
    # Size of text chunks for processing (default: 100 characters)
    chunk_size: Optional[int] = 100
    
    # Overlap size between chunks (default: 20 characters)
    overlap_size: Optional[int] = 20
    
    # Flag to reset processing (0 = no reset, 1 = reset)
    do_reset: Optional[int] = 0 



