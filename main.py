from fastapi import FastAPI

from models.base import init
from routers.v1.todo_router import todo_router
from routers.v1.user_router import user_router

init()

app = FastAPI(
    title="Todo Backend API",
    description="A simple todo application api with basic functionality",
    version="0.0.1",
)

app.include_router(user_router)
app.include_router(todo_router)
