from fastapi import Depends
from src.app.repositories.notification import NotificationRepository
from src.app.repositories.user import UserRepository
from sqlalchemy.ext.asyncio import AsyncSession
from src.app.dependencies.database import get_db_session


def get_notification_repository(
    session: AsyncSession = Depends(get_db_session),
) -> NotificationRepository:
    return NotificationRepository(session)


def get_user_repository(
    session: AsyncSession = Depends(get_db_session),
) -> UserRepository:
    return UserRepository(session)
