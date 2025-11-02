from fastapi import APIRouter, Depends, status, Body
from src.app.schemas.notification import NotificationSendRequest, NotificationResponse
from src.app.services.notification_service import NotificationService
from src.app.dependencies.services import get_notification_service

router = APIRouter(prefix="/notifications", tags=["notifications"])


@router.post(
    "/send", response_model=NotificationResponse, status_code=status.HTTP_200_OK
)
async def send_notification(
    request: NotificationSendRequest = Body(...),
    notification_service: NotificationService = Depends(get_notification_service),
):
    notification = await notification_service.send_notification(
        user_id=request.user_id,
        body=request.body,
    )
    return notification
