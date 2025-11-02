from src.app.services.channels.base import BaseChannel
from src.app.models.notification import NotificationChannel
import random


class TelegramChannel(BaseChannel):
    @property
    def channel(self) -> NotificationChannel:
        return NotificationChannel.TELEGRAM

    async def send(self, recipient: str, body: str, subject: str | None = None) -> bool:
        return random.choice([True, False])
