from .BaseController import BaseController
from .ProjectController import ProjectController
import os 
from langchain_community.document_loaders import TextLoader, PyMuPDFLoader
from models import ProcessingEnum
from langchain_text_splitters import RecursiveCharacterTextSplitter

class ProcessController(BaseController):
    """
    ProcessController is responsible for handling the processing of data within the application.
    
    It inherits from BaseController to utilize common functionality and settings.
    
    Attributes:
        settings (Settings): Application settings loaded from environment variables.
    """
    
    def __init__(self, project_id: str):

        super().__init__()

        self.project_id = project_id
        self.project_path = ProjectController.get_project_path(self, project_id = project_id)
    
    def get_file_extension(self, file_id: str):
        return os.path.splitext(file_id)[1].lower()
    
    def get_file_loader(self,file_id:str):

        file_ext = self.get_file_extension(file_id=file_id)
        file_path = os.path.join(self.project_path, file_id)

        if file_ext == ProcessingEnum.TXT.value:
            return TextLoader(file_path, encoding='utf-8')
        
        if file_ext == ProcessingEnum.PDF.value:
            return PyMuPDFLoader(file_path)
        return None
    
    def get_file_content(self, file_id: str):
        """
        Retrieves the content of a file based on its ID.
        
        Args:
            file_id (str): The unique identifier for the file.
        
        Returns:
            str: The content of the file if found, otherwise None.
        """
        loader = self.get_file_loader(file_id=file_id)
        return loader.load()
        
    def proess_file_content(self, file_id: str, file_content: list, chunk_size: int = 100, chunk_overlap: int = 20):
        
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            length_function=len
        )

        file_content_texts = [
            rec.page_content
            for rec in file_content
        ]

        file_content_metadata = [
            rec.metadata
            for rec in file_content
        ]

        chunks = text_splitter.create_documents(file_content_texts, metadatas=file_content_metadata)

        return chunks