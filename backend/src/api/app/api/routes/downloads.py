from fastapi import APIRouter, Depends

from api.app.dependencies import get_download_service
from api.app.schemas.download import DownloadRequest, DownloadResponse
from api.app.services.download_service import DownloadService

router = APIRouter()


@router.get("/status")
async def download_status(
    service: DownloadService = Depends(get_download_service),
):
    return await service.get_status()


@router.post("/", response_model=DownloadResponse)
async def create_download(
    request: DownloadRequest,
    service: DownloadService = Depends(get_download_service),
):
    return DownloadResponse(
        message="Download request received",
        url=str(request.url),
        status="pending",
    )