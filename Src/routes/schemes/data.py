"""
Data Request Schema Module
==========================

This module defines the Pydantic model for data processing request
validation. It provides structured input validation for file processing
operations including chunking parameters.

Dependencies:
- pydantic: For data validation and model definition
- typing: For type hints
"""

# Step 1: Import Pydantic and typing dependencies
from pydantic import BaseModel
from typing import Optional

class ProcessRequest(BaseModel):
    """
    Defines the structure and validation rules for file processing requests.
    """
    # Step 2: File identifier for processing
    file_id: str = None
    # Step 3: Size of text chunks for processing (default: 100 characters)
    chunk_size: Optional[int] = 100
    # Step 4: Overlap size between chunks (default: 20 characters)
    overlap_size: Optional[int] = 20
    # Step 5: Flag to reset processing (0 = no reset, 1 = reset)
    do_reset: Optional[int] = 0
    # Usage example:
    #   req = ProcessRequest(file_id='file.txt', chunk_size=200, overlap_size=30, do_reset=1)



