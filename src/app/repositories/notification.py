from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from src.app.repositories.base import BaseRepository
from src.app.models.notification import Notification, NotificationStatus


class NotificationRepository(BaseRepository[Notification]):
    def __init__(self, session: AsyncSession):
        super().__init__(Notification, session)

    async def get_by_status(self, status: NotificationStatus) -> List[Notification]:
        result = await self.session.execute(
            select(Notification).where(Notification.status == status)
        )
        return list(result.scalars().all())
