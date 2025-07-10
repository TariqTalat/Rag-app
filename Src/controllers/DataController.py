from .BaseController import BaseController
from fastapi import UploadFile
base_router = APIRouter()

class DataController(BaseController):

    def __init__(self):
        super().__init__()
        self.size_scale = 1024 * 1024  # 1 MB
    
    def validate_file(self, file: UploadFile):
        """
        Validate the uploaded file based on allowed extensions and size.

        Args:
            file (UploadFile): The file to be validated.

        Raises:
            ValueError: If the file extension is not allowed or if the file size exceeds the maximum limit.
        """
        if file.content_type not in self.app_settings.FILE_ALLOWED_TYPES:
            return False
        if file.size > self.app_settings.FILE_MAX_SIZE * self.size_scale:
            return False
        return True