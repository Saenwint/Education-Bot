from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String

from models.base import Base

class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    tg_id: Mapped[str] = mapped_column(String(400))
    username: Mapped[str] = mapped_column(String(400))
    