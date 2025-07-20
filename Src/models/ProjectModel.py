"""
Project Model Module
====================

Stepwise Breakdown:
-------------------
1. Import dependencies and base data model.
2. Define the ProjectModel class for project database operations.
3. Implement methods for creating, retrieving, and listing projects.

This module provides the data model for handling project records in the database.
It supports creating, retrieving, and paginating project documents.

Dependencies:
- .BaseDataModel: Base class for MongoDB operations
- .db_schemes.Project: Pydantic model for project schema
- .enums.DataBaseEnum: Enum for collection names
"""

from .BaseDataModel import BaseDataModel
from .db_schemes import Project
from .enums.DataBaseEnum import DataBaseEnum

class ProjectModel(BaseDataModel):
    """
    Project Model Class
    -------------------
    Handles database operations for projects, including creation,
    retrieval, and pagination.

    Example usage:
        >>> pm = ProjectModel(db_client)
        >>> project = await pm.get_project_or_create_one('proj1')
        >>> all_projects, total_pages = await pm.get_all_projects(page=1, page_size=10)
    """

    def __init__(self, db_client: object):
        """
        Initialize the project model with a database client.

        Args:
            db_client (object): MongoDB client instance

        Example usage:
            >>> pm = ProjectModel(db_client)
        """
        # Step 1: Initialize base data model
        super().__init__(db_client=db_client)
        # Step 2: Set collection for projects
        self.collection = self.db_client[DataBaseEnum.COLLECTION_PROJECT_NAME.value]

    async def create_project(self, project: Project):
        """
        Create a new project document in the database.

        Args:
            project (Project): The project data to insert
        Returns:
            Project: The inserted project with its MongoDB ID

        Example usage:
            >>> created = await pm.create_project(project)
        """
        # Step 1: Insert project document
        result = await self.collection.insert_one(project.dict(by_alias=True, exclude_unset=True))
        # Step 2: Assign inserted ID to project
        project._id = result.inserted_id
        # Step 3: Return the project
        return project

    async def get_project_or_create_one(self, project_id: str):
        """
        Retrieve a project by its ID, or create it if not found.

        Args:
            project_id (str): The project identifier
        Returns:
            Project: The found or newly created project

        Example usage:
            >>> project = await pm.get_project_or_create_one('proj1')
        """
        # Step 1: Query for project by project_id
        record = await self.collection.find_one({"project_id": project_id})
        # Step 2: If not found, create new project
        if record is None:
            project = Project(project_id=project_id)
            project = await self.create_project(project=project)
            return project
        # Step 3: Return found project
        return Project(**record)

    async def get_all_projects(self, page: int=1, page_size: int=10):
        """
        Retrieve all projects with pagination.

        Args:
            page (int): Page number (default: 1)
            page_size (int): Number of projects per page (default: 10)
        Returns:
            tuple: (list of Project, int) - List of projects and total number of pages

        Example usage:
            >>> projects, total_pages = await pm.get_all_projects(page=1, page_size=10)
        """
        # Step 1: Count total number of documents
        total_documents = await self.collection.count_documents({})
        # Step 2: Calculate total number of pages
        total_pages = total_documents // page_size
        if total_documents % page_size > 0:
            total_pages += 1
        # Step 3: Query for projects with skip and limit
        cursor = self.collection.find().skip((page-1) * page_size).limit(page_size)
        projects = []
        # Step 4: Collect projects from cursor
        async for document in cursor:
            projects.append(Project(**document))
        # Step 5: Return projects and total pages
        return projects, total_pages