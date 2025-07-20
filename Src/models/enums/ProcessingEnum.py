"""
Processing Enum Module
======================

This module defines enumeration constants for supported file types
in the processing pipeline. These enums ensure consistent file
type handling across the application.

Used by:
- controllers/ProcessController.py: For file type detection and processing
"""

from enum import Enum

class ProcessingEnum(Enum):
    """
    File Processing Types Enum
    
    Defines supported file extensions for processing operations.
    These extensions are used to determine the appropriate
    file loader and processing method.
    
    Enum Values:
        TXT: Text file extension
        PDF: PDF file extension
    """
    # Text file extension for plain text processing
    TXT = ".txt"
    
    # PDF file extension for PDF document processing
    PDF = ".pdf"