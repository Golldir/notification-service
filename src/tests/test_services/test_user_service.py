import pytest
from src.app.services.user_service import UserService
from src.app.schemas.user import UserCreate


@pytest.mark.asyncio
async def test_create_user(mock_user_repo, sample_user, mocker):
    user_data = UserCreate(
        email="test@example.com", phone="+1234567890", telegram_id="123456789"
    )

    mock_user_repo.create = mocker.AsyncMock(return_value=sample_user)

    service = UserService(mock_user_repo)
    result = await service.create_user(user_data)

    assert result == sample_user
    mock_user_repo.create.assert_called_once()


@pytest.mark.asyncio
async def test_create_user_minimal(mock_user_repo, sample_user, mocker):
    user_data = UserCreate(email="test@example.com")

    mock_user_repo.create = mocker.AsyncMock(return_value=sample_user)

    service = UserService(mock_user_repo)
    result = await service.create_user(user_data)

    assert result == sample_user
