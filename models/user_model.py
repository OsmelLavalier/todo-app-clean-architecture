from sqlalchemy import Column, String
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import relationship

from configs.base import Base


class User(Base):
    __tablename__ = "user"

    id = Column(
        INTEGER(unsigned=True),
        primary_key=True,
        autoincrement=True,
        index=True,
    )
    username = Column(String(255), unique=True, nullable=False, index=True)
    password = Column(String(255), nullable=False)

    todos = relationship("Todo", cascade="all, delete-orphan", lazy="joined")

    def __repr__(self) -> str:
        return f"User<{self.id}>"
