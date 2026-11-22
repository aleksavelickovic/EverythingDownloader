from fastapi import Depends

from api.app.core.config import Settings, get_settings
from api.app.services.download_service import DownloadService


def get_download_service(
    settings: Settings = Depends(get_settings),
) -> DownloadService:
    return DownloadService(settings=settings)
