from functools import lru_cache

from pydantic import BaseSettings


class Environment(BaseSettings):
    MYSQL_ROOT_USER: str
    MYSQL_ROOT_PASSWORD: str
    MYSQL_DATABASE: str
    MYSQL_HOST: str

    class Config:
        env_file = ".env"


@lru_cache()
def get_env():
    return Environment()
