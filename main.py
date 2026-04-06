from fastapi import FastAPI
import uvicorn

from app.core.config import settings
from app.api.routes import router as api_router

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="A simple API for face recognition and age prediction built for an MLOps pipeline.",
    version=settings.VERSION
)

# Include the API router defined in app/api/routes.py
app.include_router(api_router)

if __name__ == "__main__":
    # Run the server locally using Uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
