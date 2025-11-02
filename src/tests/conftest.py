import pytest
from uuid import uuid4
from src.app.models.user import User
from src.app.models.notification import Notification, NotificationStatus
from src.app.repositories.user import UserRepository
from src.app.repositories.notification import NotificationRepository


@pytest.fixture
def mock_session(mocker):
    return mocker.AsyncMock()


@pytest.fixture
def mock_user_repo(mock_session):
    repo = UserRepository(mock_session)
    return repo


@pytest.fixture
def mock_notification_repo(mock_session):
    repo = NotificationRepository(mock_session)
    return repo


@pytest.fixture
def sample_user():
    user = User()
    user.id = uuid4()
    user.email = "test@example.com"
    user.phone = "+1234567890"
    user.telegram_id = "123456789"
    # Для getattr в notification_service
    user.sms = user.phone
    user.telegram = user.telegram_id
    return user


@pytest.fixture
def sample_notification():
    notification = Notification()
    notification.id = uuid4()
    notification.recipient_email = "test@example.com"
    notification.body_text = "Test message"
    notification.status = NotificationStatus.PENDING
    return notification
