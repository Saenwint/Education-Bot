from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, Time

from models.base import Base

class Courses(Base):
    __tablename__ = "courses"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    link: Mapped[str] = mapped_column(String(150))
    description: Mapped[str] = mapped_column(String(150))


class Materials(Base):
    __tablename__ = "materials"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    link: Mapped[str] = mapped_column(String(150))
    description: Mapped[str] = mapped_column(String(150))