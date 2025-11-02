import pytest
from uuid import uuid4
from fastapi import HTTPException
from src.app.services.notification_service import NotificationService
from src.app.models.notification import NotificationStatus
from src.app.services.channels.email import EmailChannel


@pytest.mark.asyncio
async def test_send_notification_success(
    mock_notification_repo, mock_user_repo, sample_user, sample_notification, mocker
):
    channels = {
        "email": EmailChannel(),
        "phone": mocker.Mock(send=mocker.AsyncMock(return_value=True)),
        "telegram_id": mocker.Mock(send=mocker.AsyncMock(return_value=True)),
    }

    mock_user_repo.get_by_id = mocker.AsyncMock(return_value=sample_user)
    mock_notification_repo.create = mocker.AsyncMock(return_value=sample_notification)
    mock_notification_repo.update = mocker.AsyncMock(return_value=sample_notification)

    service = NotificationService(mock_notification_repo, mock_user_repo, channels)

    result = await service.send_notification(user_id=sample_user.id, body="Test")

    assert result["status"] == NotificationStatus.SENT
    assert "channel_used" in result
    mock_notification_repo.create.assert_called_once()


@pytest.mark.asyncio
async def test_send_notification_user_not_found(
    mock_notification_repo, mock_user_repo, mocker
):
    channels = {"email": EmailChannel()}
    mock_user_repo.get_by_id = mocker.AsyncMock(return_value=None)

    service = NotificationService(mock_notification_repo, mock_user_repo, channels)

    with pytest.raises(HTTPException) as exc:
        await service.send_notification(user_id=uuid4(), body="Test")

    assert exc.value.status_code == 404


@pytest.mark.asyncio
async def test_send_notification_all_channels_fail(
    mock_notification_repo, mock_user_repo, sample_user, sample_notification, mocker
):
    channels = {
        "email": mocker.Mock(send=mocker.AsyncMock(return_value=False)),
        "phone": mocker.Mock(send=mocker.AsyncMock(return_value=False)),
        "telegram_id": mocker.Mock(send=mocker.AsyncMock(return_value=False)),
    }

    mock_user_repo.get_by_id = mocker.AsyncMock(return_value=sample_user)
    mock_notification_repo.create = mocker.AsyncMock(return_value=sample_notification)
    mock_notification_repo.update = mocker.AsyncMock()

    service = NotificationService(mock_notification_repo, mock_user_repo, channels)

    with pytest.raises(HTTPException) as exc:
        await service.send_notification(user_id=sample_user.id, body="Test")

    assert exc.value.status_code == 500
