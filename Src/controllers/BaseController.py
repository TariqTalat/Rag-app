from helpers.config import get_settings, Settings

class BaseController:

    def __init__(self, app_settings: Settings = Depends(get_settings)):
        """
        Initialize the BaseController with application settings.

        Args:
            app_settings (Settings): The application settings.
        """
        self.app_settings = app_settings

    def get_app_settings(self):
        """
        Get the application settings.

        Returns:
            Settings: The application settings.
        """
        return self.app_settings
