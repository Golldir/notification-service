from uuid import UUID
from pydantic import BaseModel
from src.app.models.notification import NotificationStatus, NotificationChannel


class NotificationSendRequest(BaseModel):
    user_id: UUID
    body: str


class NotificationResponse(BaseModel):
    id: UUID
    channel_used: NotificationChannel | None = None
    status: NotificationStatus
