from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession, create_async_engine

from models.base import Base
from user.models import User
from timesheet.models import Timesheet
from materials.models import Courses, Materials
from config import config

engine = create_async_engine(
        config.DATABASE_URL,
        echo=True,
)

session_maker = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

async def create_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def drop_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)