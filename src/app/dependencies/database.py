from fastapi import Request, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import AsyncGenerator
from src.app.core.database import DatabaseConnection


def get_database_connection(request: Request) -> DatabaseConnection:
    """Получить DatabaseConnection из app.state (singleton)"""
    if not hasattr(request.app.state, "database"):
        raise RuntimeError("DatabaseConnection not initialized. Check lifespan.")

    return request.app.state.database


async def get_db_session(
    db_connection: DatabaseConnection = Depends(get_database_connection),
) -> AsyncGenerator[AsyncSession, None]:
    """Создает новую DB сессию на каждый HTTP запрос с авто-commit/rollback.

    Сессия автоматически коммитится при успешном завершении или откатывается при ошибке.
    """
    session_factory = db_connection.get_session_factory()

    if session_factory is None:
        raise RuntimeError("Database session factory not initialized")

    async with session_factory() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()
