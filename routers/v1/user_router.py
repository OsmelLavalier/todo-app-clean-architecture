from fastapi import APIRouter, Depends
from starlette import status

from schemas.pydantic.user_schema import UserCreate, User
from services.user_service import UserService

user_router = APIRouter(prefix="/v1/user", tags=["User"])


@user_router.get("/get", status_code=status.HTTP_200_OK, response_model=User)
async def get_user(username: str, svc: UserService = Depends()):
    """Get user by username"""
    return svc.get_by_username(username=username)


@user_router.post("/create", status_code=status.HTTP_201_CREATED, response_model=User)
async def create_user(user: UserCreate, svc: UserService = Depends()):
    return svc.create(user=user)


@user_router.delete("/delete", status_code=status.HTTP_200_OK)
async def delete_user(user_id: int, svc: UserService = Depends()):
    return svc.delete(user_id=user_id)
