from fastapi import Depends
from sqlalchemy.orm import Session

from configs.base import get_db


class DBRepository:
    def __init__(self, db: Session = Depends(get_db)) -> None:
        self.db = db
