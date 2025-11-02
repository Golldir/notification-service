from src.app.repositories.user import UserRepository
from src.app.models.user import User
from src.app.schemas.user import UserCreate


class UserService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    async def create_user(self, user_data: UserCreate) -> User:
        user = await self.user_repo.create(**user_data.model_dump())
        return user
