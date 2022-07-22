import sys
import subprocess
from fastapi import FastAPI

from routers.v1.todo_router import todo_router
from routers.v1.user_router import user_router

try:
    print("Applying latest migration...")
    process = subprocess.run(
        "alembic upgrade head",
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=True,
    )
    if process.returncode != 0:
        raise Exception("Unable to run latest migrations...")
except:
    sys.exit(1)


app = FastAPI(
    title="Todo Backend API",
    description="A simple todo application api with basic functionality",
    version="0.0.1",
)

app.include_router(user_router)
app.include_router(todo_router)
