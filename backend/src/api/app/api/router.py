from fastapi import APIRouter

from api.app.api.routes import downloads, health

api_router = APIRouter()

api_router.include_router(health.router, tags=["Health"])
api_router.include_router(
    downloads.router,
    prefix="/downloads",
    tags=["Downloads"],
)