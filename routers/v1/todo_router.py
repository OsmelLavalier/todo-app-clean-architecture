from typing import List

from fastapi import APIRouter, Depends
from starlette import status

from schemas.pydantic.todo_schema import TodoCreate, Todo
from services.todo_service import TodoService
from utils.state import State

todo_router = APIRouter(prefix="/v1/todo", tags=["Todo"])


@todo_router.get("/get", status_code=status.HTTP_200_OK, response_model=Todo)
async def get_todo(todo_id: int, svc: TodoService = Depends()):
    """Get todo"""
    return svc.get(todo_id=todo_id)


@todo_router.post("/create", status_code=status.HTTP_201_CREATED, response_model=Todo)
async def create_todo(
    todo: TodoCreate, user_id: int, state: State, svc: TodoService = Depends()
):
    """Create todo"""
    return svc.create(todo=todo, user_id=user_id, state=state.value)


@todo_router.delete("/delete", status_code=status.HTTP_200_OK)
async def delete_todo(todo_id: int, svc: TodoService = Depends()):
    """Delete todo"""
    return svc.delete(todo_id=todo_id)


@todo_router.get("/filter", status_code=status.HTTP_200_OK, response_model=List[Todo])
async def filter_todos(state: State, svc: TodoService = Depends()):
    """Filter todo by state"""
    return svc.list_by_state(state=state.value)
