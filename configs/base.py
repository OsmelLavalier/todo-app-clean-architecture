from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from .env import get_env

settings = get_env()

DATABASE_URL = f"mysql://{settings.MYSQL_ROOT_USER}:{settings.MYSQL_ROOT_PASSWORD}@{settings.MYSQL_HOST}:3306/{settings.MYSQL_DATABASE}?charset=utf8mb4"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
