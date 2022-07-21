from typing import Generator, Any

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import create_database, drop_database, database_exists

import main
from configs.base import Base, get_db
from configs.env import get_env
from routers.v1.todo_router import todo_router
from routers.v1.user_router import user_router
from schemas.pydantic.todo_schema import TodoCreate
from schemas.pydantic.user_schema import UserCreate
from services.todo_service import TodoService
from services.user_service import UserService

TEST_DATABASE_URI = (
    f"mysql://{get_env().MYSQL_ROOT_USER}:{get_env().MYSQL_ROOT_PASSWORD}@db:3306/test"
)
engine = create_engine(TEST_DATABASE_URI)
SessionTesting = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="session")
def app() -> Generator[FastAPI, Any, None]:
    if not database_exists(TEST_DATABASE_URI):
        create_database(TEST_DATABASE_URI)
        Base.metadata.create_all(bind=engine)

    _app = main.app
    _app.include_router(user_router)
    _app.include_router(todo_router)

    yield _app
    Base.metadata.drop_all(bind=engine)
    drop_database(TEST_DATABASE_URI)


@pytest.fixture(scope="session")
def db_session(app: FastAPI) -> Generator[SessionTesting, Any, None]:
    with SessionTesting() as session:
        yield session


@pytest.fixture(scope="module")
def client(
    app: FastAPI, db_session: SessionTesting
) -> Generator[TestClient, Any, None]:
    def _get_test_db():
        try:
            yield db_session
        finally:
            pass

    app.dependency_overrides[get_db] = _get_test_db
    with TestClient(app) as client:
        yield client


@pytest.fixture(scope="function")
def create_user():
    def wrapper(user: UserCreate):
        with SessionTesting() as session:
            return UserService(session).create(user=user)

    return wrapper


@pytest.fixture(scope="function")
def get_user_by_id():
    def wrapper(user_id: int):
        with SessionTesting() as session:
            return UserService(session).get_by_id(user_id=user_id)

    return wrapper


@pytest.fixture(scope="function")
def create_todo():
    def wrapper(todo: TodoCreate, state: str):
        with SessionTesting() as session:
            return TodoService(session).create(todo=todo)

    return wrapper


@pytest.fixture(scope="function")
def get_user_by_username():
    def wrapper(username: str):
        with SessionTesting() as session:
            return UserService(session).get_by_username(username=username)

    return wrapper


@pytest.fixture(scope="function")
def get_todo():
    def wrapper(todo_id: int):
        with SessionTesting() as session:
            return TodoService(session).get(todo_id=todo_id)

    return wrapper


@pytest.fixture(scope="function")
def delete_user():
    def wrapper(user_id: int):
        with SessionTesting() as session:
            return UserService(session).delete(user_id=user_id)

    return wrapper


@pytest.fixture(scope="function")
def delete_todo():
    def wrapper(todo_id: int):
        with SessionTesting() as session:
            return TodoService(session).delete(todo_id=todo_id)

    return wrapper
