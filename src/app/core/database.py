from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncSession,
    async_sessionmaker,
    AsyncEngine,
)
from sqlalchemy import text
from typing import Optional


class DatabaseConnection:
    def __init__(self, db_url: str):
        self.db_url = db_url
        self.async_engine: Optional[AsyncEngine] = None
        self.session_factory: Optional[async_sessionmaker[AsyncSession]] = None

    def get_engine(self) -> Optional[AsyncEngine]:
        """Получить async engine"""
        return self.async_engine

    def get_session_factory(self) -> Optional[async_sessionmaker[AsyncSession]]:
        """Получить фабрику для создания сессий"""
        return self.session_factory

    async def open_connection(self) -> None:
        self.async_engine = create_async_engine(self.db_url)
        self.session_factory = async_sessionmaker(
            bind=self.async_engine, expire_on_commit=False
        )

    async def check_connection(self) -> bool:
        """Проверить подключение к базе данных"""
        if self.async_engine is None:
            print(
                "❌ Подключение к БД не установлено. Вызовите open_connection() сначала."
            )
            return False

        try:
            async with self.async_engine.begin() as conn:
                await conn.execute(text("SELECT 1"))
            print("✅ Подключение к БД успешно установлено")
            return True
        except Exception as e:
            print(f"❌ Ошибка подключения к БД: {e}")
            return False

    async def close_connection(self) -> None:
        if self.async_engine is not None:
            await self.async_engine.dispose()
            self.async_engine = None
            self.session_factory = None
