from typing import List

from models.todo_model import Todo
from schemas.pydantic.todo_schema import TodoCreate
from .base import DBRepository


class TodoRepository(DBRepository):
    def get(self, todo_id: int) -> Todo:
        return self.db.query(Todo).filter_by(id=todo_id).first()

    def create(self, todo: TodoCreate, user_id: int, state: str) -> Todo:
        db_todo = Todo(**todo.dict(), user_id=user_id, state=state)
        self.db.add(db_todo)
        self.db.commit()
        self.db.refresh(db_todo)
        return db_todo

    def delete(self, todo_id: int) -> None:
        db_todo = self.db.query(Todo).filter_by(id=todo_id).first()
        self.db.delete(db_todo)
        self.db.commit()

    def list_by_state(self, state: str) -> List[Todo]:
        return self.db.query(Todo).filter_by(state=state).all()
