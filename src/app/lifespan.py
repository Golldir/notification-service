from fastapi import FastAPI
from src.app.core.database import DatabaseConnection
from src.app.core.config import settings
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI) -> None:
    database = DatabaseConnection(db_url=settings.db_url)
    await database.open_connection()
    await database.check_connection()

    app.state.database: DatabaseConnection = database

    yield

    await database.close_connection()
