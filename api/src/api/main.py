from fastapi import FastAPI

app = FastAPI(
    title="Everything Downloader API",
    description="FastAPI backend for Everything Downloader",
    version="1.0.0"
)


@app.get("/")
async def root():
    return {
        "message": "Hello World!"
    }


@app.get("/health")
async def health():
    return {
        "status": "healthy"
    }
