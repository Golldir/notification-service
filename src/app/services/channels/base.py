from abc import ABC, abstractmethod
from src.app.models.notification import NotificationChannel


class BaseChannel(ABC):
    @property
    @abstractmethod
    def channel(self) -> NotificationChannel:
        pass

    @abstractmethod
    async def send(self, recipient: str, body: str, subject: str | None = None) -> bool:
        pass
