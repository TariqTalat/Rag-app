from enum import Enum

class AssetTypeEnum(Enum):
    """
    Enum for asset types in the application.
    This enum is used to define the types of assets
    that can be associated with projects, ensuring
    consistency and avoiding hard-coded strings throughout the codebase.
    """

    FILE = "file"