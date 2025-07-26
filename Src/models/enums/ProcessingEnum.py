"""
Processing Enum Module
======================

This module defines enumeration constants for supported file types
in the processing pipeline. These enums ensure consistent file
type handling across the application.

Dependencies:
- enum: For defining enumeration types
"""

# Step 1: Import Enum from the enum module
from enum import Enum

class ProcessingEnum(Enum):
    """
    Defines supported file extensions for processing operations.
    """
    # Step 2: Text file extension for plain text processing
    TXT = ".txt"
    # Step 3: PDF file extension for PDF document processing
    PDF = ".pdf"
    # Usage example:
    #   ProcessingEnum.TXT.value -> '.txt'