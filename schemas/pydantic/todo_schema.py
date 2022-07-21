from datetime import datetime

from pydantic import BaseModel

from utils.state import State


class TodoBase(BaseModel):
    name: str
    data: str


class TodoCreate(TodoBase):
    pass


class Todo(TodoBase):
    id: int
    created_at: datetime
    user_id: int
    state: str = State.NEW.value

    class Config:
        orm_mode = True
        json_encoders = {datetime: lambda dt: dt.strftime("%Y:%m:%d %H:%M:%S")}
