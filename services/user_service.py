from typing import Union, List

from fastapi import HTTPException
from starlette import status

from repositories.user_repository import UserRepository
from schemas.pydantic.user_schema import UserCreate, User
from utils.validator import validate_username, hash_password


class UserService(UserRepository):
    def get_by_username(self, username: str) -> Union[User, HTTPException]:
        user = UserRepository(self.db).get_by_username(username)

        if not user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="User not found",
            )
        return User.from_orm(user)

    def get_by_id(self, user_id: int) -> Union[User, HTTPException]:
        user = UserRepository(self.db).get_by_id(user_id)

        if not user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="User not found",
            )
        return User.from_orm(user)

    def list(self) -> List[User]:
        return UserRepository(self.db).list()

    def create(self, user: UserCreate) -> Union[User, HTTPException]:
        found_user = UserRepository(self.db).get_by_username(username=user.username)
        if found_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="User already exists",
            )
        if not validate_username(username=user.username):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Username may contain invalid " "characters",
            )
        user.password = hash_password(user.password)
        return User.from_orm(UserRepository(self.db).create(user))

    def delete(self, user_id: int) -> Union[str, HTTPException]:
        user = self.get_by_id(user_id=user_id)
        return f"User {user.username} was successfully deleted"
