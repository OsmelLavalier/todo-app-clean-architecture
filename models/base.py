from sqlalchemy_utils import create_database, database_exists

from configs.base import DATABASE_URL, engine, Base


def init():
    if not database_exists(DATABASE_URL):
        create_database(DATABASE_URL)
        Base.metadata.create_all(bind=engine)
