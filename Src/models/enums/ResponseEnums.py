from enum import Enum

class ResponseSignals(Enum):

    FILE_VALIDATE_SUCCESS = "file validation successful"
    FILE_VALIDATE_FAIL = "file validation failed"
    FILE_NOT_FOUND = "file not found"
    FILE_TYPE_NOT_SUPPORTED = "file type not supported"
    FILE_SIZE_EXCEEDED = "file size exceeded"
    FILE_UPLOAD_SUCCESS = "file uploaded successfully"
    FILE_UPLOADED_FAIL = "file upload failed"