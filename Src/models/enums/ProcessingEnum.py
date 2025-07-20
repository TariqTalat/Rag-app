"""
Processing Enum Module
======================

Stepwise Breakdown:
-------------------
1. Import Enum from the enum module.
2. Define the ProcessingEnum class for supported file types.
3. Add enum values for TXT and PDF file extensions.

This module defines enumeration constants for supported file types
in the processing pipeline. These enums ensure consistent file
type handling across the application.

Dependencies:
- enum: For defining enumeration types
"""

from enum import Enum

class ProcessingEnum(Enum):
    """
    File Processing Types Enum
    -------------------------
    Defines supported file extensions for processing operations.
    These extensions are used to determine the appropriate
    file loader and processing method.

    Enum Values:
        TXT: Text file extension
        PDF: PDF file extension

    Example usage:
        >>> ProcessingEnum.TXT.value
        '.txt'
    """
    # Step 1: Text file extension for plain text processing
    TXT = ".txt"
    # Step 2: PDF file extension for PDF document processing
    PDF = ".pdf"