from uuid import UUID
from src.app.models.notification import NotificationStatus, NotificationChannel
from src.app.repositories.notification import NotificationRepository
from src.app.repositories.user import UserRepository
from src.app.services.channels.base import BaseChannel
from fastapi import HTTPException


class NotificationService:
    def __init__(
        self,
        notification_repo: NotificationRepository,
        user_repo: UserRepository,
        channels: dict[str, BaseChannel],
    ) -> None:
        self.notification_repo = notification_repo
        self.user_repo = user_repo
        self.channels = channels

    async def send_notification(
        self,
        user_id: UUID,
        body: str = "",
    ):
        user = await self.user_repo.get_by_id(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        notification = await self.notification_repo.create(
            recipient_email=user.email,
            recipient_phone=user.phone,
            recipient_telegram_id=user.telegram_id,
            body_text=body,
            status=NotificationStatus.PENDING,
        )

        for channel_type, channel in self.channels.items():
            recipient = getattr(user, channel_type)
            if not recipient:
                continue

            success = await channel.send(recipient, body)
            if success:
                channel_enum = NotificationChannel(channel_type)
                await self.notification_repo.update(
                    notification.id,
                    channel_used=channel_enum,
                    status=NotificationStatus.SENT,
                )
                return {
                    "id": notification.id,
                    "channel_used": channel_enum,
                    "status": NotificationStatus.SENT,
                }

        await self.notification_repo.update(
            notification.id,
            status=NotificationStatus.FAILED,
        )
        raise HTTPException(status_code=500, detail="Failed to send notification")
