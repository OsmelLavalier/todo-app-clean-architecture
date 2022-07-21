from datetime import datetime

from sqlalchemy import Column, String, DATETIME, ForeignKey
from sqlalchemy.dialects.mysql import INTEGER

from configs.base import Base


class Todo(Base):
    __tablename__ = "todo"

    id = Column(
        INTEGER(unsigned=True),
        primary_key=True,
        autoincrement=True,
        index=True,
    )
    created_at = Column(DATETIME, nullable=True, default=datetime.now())
    name = Column(String(255), nullable=False, index=True)
    data = Column(String(255), nullable=False)
    user_id = Column(
        INTEGER(unsigned=True),
        ForeignKey("user.id", ondelete="CASCADE"),
        index=True,
    )
    state = Column(String(255), nullable=False)

    def __repr__(self) -> str:
        return f"Todo<{self.id}>"
