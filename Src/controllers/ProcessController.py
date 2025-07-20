"""
Process Controller Module
=========================

This module handles file processing operations including text extraction,
chunking, and content management. It provides the core functionality
for processing uploaded files into searchable chunks for RAG operations.

Dependencies:
- .BaseController: Inherits from BaseController for common functionality
- .ProjectController: For project directory management
- os: For file system operations
- langchain_community.document_loaders: For file content extraction
- models.ProcessingEnum: For file type detection
- langchain_text_splitters: For text chunking operations

Used by:
- routes/data.py: For file processing endpoints
"""

from .BaseController import BaseController
from .ProjectController import ProjectController
import os 
from langchain_community.document_loaders import TextLoader, PyMuPDFLoader
from models import ProcessingEnum
from langchain_text_splitters import RecursiveCharacterTextSplitter

class ProcessController(BaseController):
    """
    Process Controller Class
    
    Handles file processing operations including content extraction,
    text chunking, and document management. It extends BaseController
    to inherit common functionality while providing specialized
    processing capabilities.
    
    Attributes:
        project_id (str): Unique identifier for the project
        project_path (str): File system path to the project directory
    
    Used by:
        - routes/data.py: For file processing endpoints
    """
    
    def __init__(self, project_id: str):
        """
        Initialize the process controller for a specific project
        
        Sets up the controller with project-specific paths and
        inherits common functionality from BaseController.
        
        Args:
            project_id (str): Unique identifier for the project
        """
        # Initialize parent class (BaseController)
        super().__init__()

        # Store project identifier for operations
        self.project_id = project_id
        
        # Get project directory path for file access
        # Used by: ProjectController.get_project_path()
        self.project_path = ProjectController.get_project_path(self, project_id=project_id)
    
    def get_file_extension(self, file_id: str):
        """
        Extract file extension from file ID
        
        Gets the file extension (including the dot) from the file ID
        and converts it to lowercase for consistent comparison.
        
        Args:
            file_id (str): File identifier with extension
        
        Returns:
            str: File extension in lowercase (e.g., '.txt', '.pdf')
        
        Used by:
            - self.get_file_loader(): For determining file type
        """
        # Extract and normalize file extension
        return os.path.splitext(file_id)[1].lower()
    
    def get_file_loader(self, file_id: str):
        """
        Get appropriate file loader based on file type
        
        Determines the correct LangChain loader to use based on
        the file extension for content extraction.
        
        Args:
            file_id (str): File identifier with extension
        
        Returns:
            DocumentLoader: LangChain loader instance or None if unsupported
        
        Used by:
            - self.get_file_content(): For loading file content
        
        Dependencies:
            - models/enums/ProcessingEnum.py: For file type detection
        """
        # Get file extension for type detection
        file_ext = self.get_file_extension(file_id=file_id)
        
        # Construct full file path
        file_path = os.path.join(self.project_path, file_id)

        # Return appropriate loader based on file type
        # Used by: models/enums/ProcessingEnum.py -> TXT
        if file_ext == ProcessingEnum.TXT.value:
            return TextLoader(file_path, encoding='utf-8')
        
        # Used by: models/enums/ProcessingEnum.py -> PDF
        if file_ext == ProcessingEnum.PDF.value:
            return PyMuPDFLoader(file_path)
        
        # Return None for unsupported file types
        return None
    
    def get_file_content(self, file_id: str):
        """
        Retrieve the content of a file based on its ID
        
        Loads and extracts content from files using appropriate
        LangChain loaders based on file type.
        
        Args:
            file_id (str): The unique identifier for the file
        
        Returns:
            list: List of document objects with content and metadata
        
        Used by:
            - self.proess_file_content(): For content processing
        """
        # Get appropriate loader for file type
        loader = self.get_file_loader(file_id=file_id)
        
        # Load and return file content
        return loader.load()
        
    def process_file_content(self, file_id: str, file_content: list, chunk_size: int = 100, chunk_overlap: int = 20):
        """
        Process file content into searchable chunks
        
        Splits file content into smaller chunks for efficient
        retrieval and processing in RAG operations.
        
        Args:
            file_id (str): File identifier for reference
            file_content (list): List of document objects from loader
            chunk_size (int): Size of each chunk (default: 100)
            chunk_overlap (int): Overlap between chunks (default: 20)
        
        Returns:
            list: List of processed document chunks
        
        Used by:
            - routes/data.py: For file processing endpoints
        """
        # Initialize text splitter with specified parameters
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            length_function=len
        )

        # Extract text content from document objects
        file_content_texts = [
            rec.page_content
            for rec in file_content
        ]

        # Extract metadata from document objects
        file_content_metadata = [
            rec.metadata
            for rec in file_content
        ]

        # Create chunks from text content with metadata
        chunks = text_splitter.create_documents(file_content_texts, metadatas=file_content_metadata)

        return chunks