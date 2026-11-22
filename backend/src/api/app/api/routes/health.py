from fastapi import APIRouter, Depends

from api.app.core.config import Settings, get_settings

router = APIRouter()


@router.get("/health")
async def health_check(
    settings: Settings = Depends(get_settings),
):
    return {
        "status": "healthy",
        "application": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "environment": settings.ENVIRONMENT,
    }
