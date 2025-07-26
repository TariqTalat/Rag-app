from enum import Enum

class LLMEnum(Enum):
    """
    Enum for LLM (Large Language Model) types.
    """
    OPENAI = "openai"
    COHERE = "cohere"

class OpenAIEnums(Enum):
    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"