from fastapi import FastAPI
from sqlalchemy import text

from app.core.config import settings
from app.core.database import engine

app = FastAPI(
    title=settings.APP_NAME,
    description="Role-Based Authentication System",
    version="1.0.0"
)

@app.get("/")
async def root():
    return {
        "message": "Welcome to Identix API"
    }

@app.get("/health")
async def health_check():

    async with engine.connect() as connection:
        await connection.execute(text("SELECT 1"))

    return {
        "status": "healthy",
        "database": "connected"
    }