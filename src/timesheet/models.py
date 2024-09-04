from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, Time

from models.base import Base

class Timesheet(Base):
    __tablename__ = "timesheet"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    group: Mapped[int] = mapped_column(Integer)
    day: Mapped[int] = mapped_column(Integer)
    week: Mapped[int] = mapped_column(Integer)
    time_start: Mapped[Time] = mapped_column(Time)
    time_end: Mapped[Time] = mapped_column(Time)
    cabinet: Mapped[int] = mapped_column(Integer)
    subject: Mapped[str] = mapped_column(String(50))
    teacher: Mapped[str] = mapped_column(String(50))
