from typing import Union, List

from fastapi import HTTPException
from starlette import status

from repositories.todo_repository import TodoRepository
from schemas.pydantic.todo_schema import Todo, TodoCreate
from services.user_service import UserService


class TodoService(TodoRepository):
    def get(self, todo_id: int) -> Union[Todo, HTTPException]:
        todo = TodoRepository(self.db).get(todo_id=todo_id)

        if not todo:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Todo not found",
            )
        return Todo.from_orm(todo)

    def create(
        self, todo: TodoCreate, user_id: int, state: str
    ) -> Union[Todo, HTTPException]:
        UserService(self.db).get_by_id(user_id=user_id)

        todo = TodoRepository(self.db).create(todo=todo, user_id=user_id, state=state)
        return Todo.from_orm(todo)

    def delete(self, todo_id: int) -> Union[str, HTTPException]:
        todo = self.get(todo_id=todo_id)
        return f"Todo {todo.name} was successfully deleted"

    def list_by_state(self, state: str) -> List[Todo]:
        return TodoRepository(self.db).list_by_state(state=state)
