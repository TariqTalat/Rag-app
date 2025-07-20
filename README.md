# Mini-RAG System

A minimal implementation of a Retrieval-Augmented Generation (RAG) system for question answering, built with FastAPI and MongoDB. This system provides file upload capabilities, project-based organization, and a foundation for building RAG applications.

## 🏗️ Project Architecture

### Directory Structure
```
mini-rag/
├── Src/
│   ├── main.py                 # FastAPI application entry point with MongoDB
│   ├── requirements.txt        # Python dependencies
│   ├── controllers/            # Business logic controllers
│   │   ├── BaseController.py   # Base controller with common functionality
│   │   ├── DataController.py   # File processing and validation
│   │   ├── ProjectController.py # Project directory management
│   │   └── __init__.py
│   ├── models/                 # Data models and enums
│   │   ├── enums/
│   │   │   └── ResponseEnums.py # Standardized response signals
│   │   └── __init__.py
│   ├── routes/                 # API route definitions
│   │   ├── base.py            # General API endpoints
│   │   ├── data.py            # File upload endpoints
│   │   └── __init__.py
│   ├── helpers/               # Utility modules
│   │   ├── config.py          # Configuration management
│   │   └── __init__.py
│   └── assets/                # Static assets and uploaded files
│       └── files/             # Project-specific file storage
└── README.md
```

### Component Connections

#### Core Components Flow
1. **main.py** → Initializes FastAPI app with MongoDB and includes routers
   - Includes `routes/base.py` → General API endpoints
   - Includes `routes/data.py` → File upload endpoints
   - Connects to MongoDB → Database operations

2. **routes/data.py** → File upload endpoint
   - Uses `DataController` → File validation and processing
   - Uses `ProjectController` → Project directory management
   - Uses `helpers/config.py` → Application settings
   - Uses `models/ResponseEnums.py` → Standardized responses

3. **controllers/DataController.py** → File processing logic
   - Inherits from `BaseController` → Common functionality
   - Uses `ProjectController` → Project path management
   - Uses `models/ResponseEnums.py` → Response signals

4. **controllers/ProjectController.py** → Project management
   - Inherits from `BaseController` → Common functionality
   - Manages project-specific directories

5. **controllers/BaseController.py** → Base functionality
   - Uses `helpers/config.py` → Application settings
   - Provides utility methods for all controllers

6. **helpers/config.py** → Configuration management
   - Uses Pydantic Settings for type-safe configuration
   - Loads from `.env` file including MongoDB settings

## 🚀 Features

- **File Upload & Validation**: Secure file upload with type and size validation
- **Project Organization**: Files organized by project ID
- **Unique File Naming**: Prevents filename conflicts with random string prefixes
- **Async File Processing**: Non-blocking file operations
- **MongoDB Integration**: Database storage for metadata and file information
- **Standardized Responses**: Consistent API response format
- **Configuration Management**: Environment-based configuration
- **Error Handling**: Comprehensive error handling and logging

## 📋 Requirements

- Python 3.8 or later
- FastAPI framework
- Uvicorn ASGI server
- MongoDB database

### Install Python using MiniConda

1. Download and install MiniConda from [here](https://docs.anaconda.com/free/miniconda/#quick-command-line-install)
2. Create a new environment using the following command:
```bash
$ conda create -n mini-rag python=3.8
```
3. Activate the environment:
```bash
$ conda activate mini-rag
```

### (Optional) Setup your command line interface for better readability

```bash
export PS1="\[\033[01;32m\]\u@\h:\w\n\[\033[00m\]\$ "
```

## 🛠️ Installation

### Install the required packages

```bash
$ pip install -r requirements.txt
```

### Setup MongoDB

1. Install MongoDB on your system
2. Start MongoDB service
3. Create a database for the application

### Setup the environment variables

```bash
$ cp .env.example .env
```

Set your environment variables in the `.env` file:

```env
# Application metadata
APP_NAME=mini-rag
APP_VERSION=1.0.0

# API configuration
OPENAI_API_KEY=your_openai_api_key_here

# File upload settings
FILE_ALLOWED_TYPES=["text/plain","application/pdf","text/csv"]
FILE_MAX_SIZE=10
FILE_DEFAULT_CHUNK_SIZE=8192

# Database configuration
MONGODB_URL=mongodb://localhost:27017
MONGODB_DATABASE=mini_rag
```

## 🚀 Running the Application

### Start the FastAPI server

```bash
$ uvicorn main:app --reload --host 0.0.0.0 --port 5000
```

The server will start on `http://localhost:5000`

## 📚 API Documentation

### Base Endpoints

#### GET `/api/v1/`
Returns application information
```json
{
  "app_name": "mini-rag",
  "app_version": "1.0.0"
}
```

### Data Endpoints

#### POST `/api/v1/data/upload/{project_id}`
Upload a file to a specific project

**Parameters:**
- `project_id` (path): Unique project identifier
- `file` (form-data): File to upload

**Success Response:**
```json
{
  "signal": "file uploaded successfully",
  "file_id": "abc123_document.pdf"
}
```

**Error Responses:**
```json
{
  "signal": "file type not supported"
}
```
```json
{
  "signal": "file size exceeded"
}
```

## 🔧 Configuration

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `APP_NAME` | Application name | `mini-rag` |
| `APP_VERSION` | Application version | `1.0.0` |
| `OPENAI_API_KEY` | OpenAI API key | Required |
| `FILE_ALLOWED_TYPES` | Allowed file types | `["text/plain","application/pdf","text/csv"]` |
| `FILE_MAX_SIZE` | Maximum file size in MB | `10` |
| `FILE_DEFAULT_CHUNK_SIZE` | File chunk size for processing | `8192` |
| `MONGODB_URL` | MongoDB connection string | `mongodb://localhost:27017` |
| `MONGODB_DATABASE` | MongoDB database name | `mini_rag` |

## 📁 File Storage

Files are stored in the following structure:
```
assets/files/
├── project_id_1/
│   ├── abc123_document1.pdf
│   └── def456_document2.txt
└── project_id_2/
    └── ghi789_document3.csv
```

Each file gets a unique name with format: `{random_string}_{cleaned_original_name}`

## 🧪 Testing

### POSTMAN Collection

Download the POSTMAN collection from [/assets/mini-rag-app.postman_collection.json](/assets/mini-rag-app.postman_collection.json)

### Example API Calls

```bash
# Get application info
curl -X GET "http://localhost:5000/api/v1/"

# Upload a file
curl -X POST "http://localhost:5000/api/v1/data/upload/my-project" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@document.pdf"
```

## 🔍 Code Documentation

### Key Classes and Their Responsibilities

1. **BaseController**: Provides common functionality for all controllers
   - Configuration management
   - File system utilities
   - Random string generation

2. **DataController**: Handles file processing operations
   - File validation (type, size)
   - Unique file path generation
   - File name sanitization

3. **ProjectController**: Manages project-specific operations
   - Project directory creation
   - Project path management

4. **Settings**: Configuration management using Pydantic
   - Environment variable loading
   - Type validation
   - Default value handling

### Response Signals

The system uses standardized response signals for consistent error handling:
- `FILE_VALIDATE_SUCCESS`: File validation passed
- `FILE_VALIDATE_FAIL`: File validation failed
- `FILE_TYPE_NOT_SUPPORTED`: Unsupported file type
- `FILE_SIZE_EXCEEDED`: File too large
- `FILE_UPLOAD_SUCCESS`: Upload successful
- `FILE_UPLOADED_FAIL`: Upload failed

### Database Integration

The application uses MongoDB for:
- File metadata storage
- Project information
- User data (future feature)
- Search indexing (future feature)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.