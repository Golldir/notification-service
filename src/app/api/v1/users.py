from fastapi import APIRouter, Depends, status, Body
from src.app.schemas.user import UserCreate, UserResponse
from src.app.services.user_service import UserService
from src.app.dependencies.services import get_user_service

router = APIRouter(prefix="/users", tags=["users"])


@router.post("", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(
    user_data: UserCreate = Body(...),
    user_service: UserService = Depends(get_user_service),
):
    user = await user_service.create_user(user_data)
    return user
