from typing import List

from pydantic import BaseModel, validator

from .todo_schema import Todo


class UserBase(BaseModel):
    username: str
    password: str

    @validator("password", pre=True)
    def validate_password_length(cls, v):
        if len(v) == 0:
            return ValueError("Password can't be empty")
        if len(v) < 5:
            return ValueError("Password must greater ")
        return v


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int
    todos: List[Todo] = []

    class Config:
        orm_mode = True
