import uuid
from datetime import datetime
from enum import Enum as PyEnum
from sqlalchemy import Column, String, Text, DateTime, Enum as SQLEnum
from sqlalchemy.dialects.postgresql import UUID
from src.app.models.base import Base


class NotificationStatus(PyEnum):
    PENDING = "pending"
    SENT = "sent"
    FAILED = "failed"


class NotificationChannel(PyEnum):
    EMAIL = "email"
    SMS = "phone"
    TELEGRAM = "telegram_id"


class Notification(Base):
    __tablename__ = "notifications"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    recipient_email = Column(String, nullable=True)
    recipient_phone = Column(String, nullable=True)
    recipient_telegram_id = Column(String, nullable=True)
    body_text = Column(Text, nullable=False)
    status = Column(
        SQLEnum(NotificationStatus), nullable=False, default=NotificationStatus.PENDING
    )
    channel_used = Column(SQLEnum(NotificationChannel), nullable=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
