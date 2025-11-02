from uuid import UUID
from pydantic import BaseModel


class UserCreate(BaseModel):
    email: str | None = None
    phone: str | None = None
    telegram_id: str | None = None


class UserResponse(BaseModel):
    id: UUID
    email: str | None
    phone: str | None
    telegram_id: str | None

    class Config:
        from_attributes = True
