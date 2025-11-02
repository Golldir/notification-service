from src.app.services.notification_service import NotificationService
from src.app.services.user_service import UserService
from src.app.repositories.notification import NotificationRepository
from src.app.repositories.user import UserRepository
from fastapi import Depends
from src.app.dependencies.repositories import (
    get_notification_repository,
    get_user_repository,
)
from src.app.dependencies.channels import get_channels


def get_user_service(
    user_repo: UserRepository = Depends(get_user_repository),
) -> UserService:
    return UserService(user_repo)


def get_notification_service(
    notification_repo: NotificationRepository = Depends(get_notification_repository),
    user_repo: UserRepository = Depends(get_user_repository),
    channels: dict = Depends(get_channels),
) -> NotificationService:
    return NotificationService(notification_repo, user_repo, channels)
