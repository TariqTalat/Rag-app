"""
Data Request Schema Module
==========================

Stepwise Breakdown:
-------------------
1. Import Pydantic and typing dependencies.
2. Define the ProcessRequest Pydantic model for file processing requests.
3. Add field defaults and validation.

This module defines the Pydantic model for data processing request
validation. It provides structured input validation for file processing
operations including chunking parameters.

Dependencies:
- pydantic: For data validation and model definition
- typing: For type hints
"""

from pydantic import BaseModel
from typing import Optional

class ProcessRequest(BaseModel):
    """
    Process Request Schema
    ----------------------
    Defines the structure and validation rules for file processing
    requests. Includes parameters for chunking configuration and
    processing options.

    Attributes:
        file_id (str): Identifier of the file to process
        chunk_size (Optional[int]): Size of text chunks (default: 100)
        overlap_size (Optional[int]): Overlap between chunks (default: 20)
        do_reset (Optional[int]): Reset processing flag (default: 0)

    Example usage:
        >>> req = ProcessRequest(file_id='file.txt', chunk_size=200, overlap_size=30, do_reset=1)
        >>> print(req.dict())
    """
    # Step 1: File identifier for processing
    file_id: str = None
    # Step 2: Size of text chunks for processing (default: 100 characters)
    chunk_size: Optional[int] = 100
    # Step 3: Overlap size between chunks (default: 20 characters)
    overlap_size: Optional[int] = 20
    # Step 4: Flag to reset processing (0 = no reset, 1 = reset)
    do_reset: Optional[int] = 0 



