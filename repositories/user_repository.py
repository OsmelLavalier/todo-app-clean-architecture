from typing import List

from models.user_model import User
from .base import DBRepository
from schemas.pydantic.user_schema import UserCreate


class UserRepository(DBRepository):
    def get_by_username(self, username: str) -> User:
        return self.db.query(User).filter_by(username=username).first()

    def get_by_id(self, user_id: int) -> User:
        return self.db.query(User).filter_by(id=user_id).first()

    def list(self) -> List[User]:
        return self.db.query(User).all()

    def create(self, user: UserCreate) -> User:
        db_user = User(**user.dict())
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def delete(self, user_id: int) -> None:
        db_user = self.db.query(User).filter_by(id=user_id).first()
        self.db.delete(db_user)
        self.db.commit()
