from api.app.core.config import Settings


class DownloadService:

    def __init__(self, settings: Settings):
        self.settings = settings

    async def get_status(self) -> dict:
        return {
            "service": "download",
            "status": "operational",
            "environment": self.settings.ENVIRONMENT,
        }