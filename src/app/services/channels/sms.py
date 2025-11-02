from src.app.services.channels.base import BaseChannel
from src.app.models.notification import NotificationChannel
import random


class SMSChannel(BaseChannel):
    @property
    def channel(self) -> NotificationChannel:
        return NotificationChannel.SMS

    async def send(self, recipient: str, body: str, subject: str | None = None) -> bool:
        # Мок: всегда успешно
        return random.choice([True, False])
