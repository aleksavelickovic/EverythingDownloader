from pydantic import BaseModel, HttpUrl


class DownloadRequest(BaseModel):
    url: HttpUrl


class DownloadResponse(BaseModel):
    message: str
    url: str
    status: str