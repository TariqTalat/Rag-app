"""
Process Controller Module
=========================

This module handles file processing operations including text extraction,
chunking, and content management for RAG workflows.

Dependencies:
- .BaseController: Base controller for shared logic
- .ProjectController: For project directory management
- os: For file system operations
- langchain_community.document_loaders: For file content extraction
- langchain_text_splitters: For text chunking
- models.ProcessingEnum: For file type detection
"""

# Step 1: Import dependencies and base controller
from .BaseController import BaseController
from .ProjectController import ProjectController
import os
from langchain_community.document_loaders import TextLoader
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from models import ProcessingEnum

class ProcessController(BaseController):
    """
    Handles file processing: extension detection, loader selection,
    content extraction, and chunking for RAG.
    """
    def __init__(self, project_id: str):
        """
        Initialize the process controller for a specific project.
        Args:
            project_id (str): The project identifier
        """
        # Step 2: Initialize base controller
        super().__init__()
        # Step 3: Store project identifier
        self.project_id = project_id
        # Step 4: Set project path for file operations
        self.project_path = ProjectController().get_project_path(project_id=project_id)

    def get_file_extension(self, file_id: str):
        """
        Extract file extension from file_id.
        Args:
            file_id (str): The file name or path
        Returns:
            str: The file extension (e.g., '.txt')
        """
        # Step 5: Extract file extension
        return os.path.splitext(file_id)[-1]

    def get_file_loader(self, file_id: str):
        """
        Return appropriate loader for supported file types or None.
        Args:
            file_id (str): The file name
        Returns:
            Loader or None: Loader instance for supported file types
        """
        # Step 6: Get file extension
        file_ext = self.get_file_extension(file_id=file_id)
        # Step 7: Build file path
        file_path = os.path.join(self.project_path, file_id)
        # Step 8: Check if file exists
        if not os.path.exists(file_path):
            return None
        # Step 9: Return loader for TXT
        if file_ext == ProcessingEnum.TXT.value:
            return TextLoader(file_path, encoding="utf-8")
        # Step 10: Return loader for PDF
        if file_ext == ProcessingEnum.PDF.value:
            return PyMuPDFLoader(file_path)
        # Step 11: Return None for unsupported types
        return None

    def get_file_content(self, file_id: str):
        """
        Load and return content if loader exists, else None.
        Args:
            file_id (str): The file name
        Returns:
            list or None: Loaded content or None if not found
        """
        # Step 12: Get loader for file
        loader = self.get_file_loader(file_id=file_id)
        # Step 13: Load content if loader exists
        if loader:
            return loader.load()
        return None

    def process_file_content(self, file_content: list, file_id: str,
                             chunk_size: int=100, overlap_size: int=20):
        """
        Split file content into chunks for RAG.
        Args:
            file_content (list): List of loaded document objects
            file_id (str): The file name
            chunk_size (int): Size of each chunk (default: 100)
            overlap_size (int): Overlap between chunks (default: 20)
        Returns:
            list: List of chunked documents
        """
        # Step 14: Initialize text splitter
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=overlap_size,
            length_function=len,
        )
        # Step 15: Extract text and metadata from file_content
        file_content_texts = [rec.page_content for rec in file_content]
        file_content_metadata = [rec.metadata for rec in file_content]
        # Step 16: Create and return chunks
        chunks = text_splitter.create_documents(
            file_content_texts,
            metadatas=file_content_metadata
        )
        return chunks