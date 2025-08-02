"""
LLM Enums Module
=================

This module defines enumerations for LLM (Large Language Model) providers
and their associated roles and document types.

Dependencies:
- enum: For creating enumerations
"""

# Import Enum for creating enumerations
from enum import Enum

class LLMEnums(Enum):
    """
    Enumeration for LLM providers.

    Attributes:
    - OPENAI: Represents OpenAI provider
    - COHERE: Represents Cohere provider
    """
    OPENAI = "OPENAI"
    COHERE = "COHERE"

class OpenAIEnums(Enum):
    """
    Enumeration for OpenAI roles.

    Attributes:
    - SYSTEM: Represents system role
    - USER: Represents user role
    - ASSISTANT: Represents assistant role
    """
    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"

class CoHereEnums(Enum):
    """
    Enumeration for Cohere roles and document types.

    Attributes:
    - SYSTEM: Represents system role
    - USER: Represents user role
    - ASSISTANT: Represents chatbot role
    - DOCUMENT: Represents search document type
    - QUERY: Represents search query type
    """
    SYSTEM = "SYSTEM"
    USER = "USER"
    ASSISTANT = "CHATBOT"

    DOCUMENT = "search_document"
    QUERY = "search_query"

class DocumentTypeEnum(Enum):
    """
    Enumeration for document types.

    Attributes:
    - DOCUMENT: Represents document type
    - QUERY: Represents query type
    """
    DOCUMENT = "document"
    QUERY = "query"