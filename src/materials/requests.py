from sqlalchemy.ext.asyncio import AsyncSession
from materials.models import Materials, Courses

from sqlalchemy import select

async def get_courses(session: AsyncSession):
    query = select(Courses)
    result = await session.execute(query)
    return result.scalars().all()


async def get_materials(session: AsyncSession):
    query = select(Materials)
    result = await session.execute(query)
    return result.scalars().all()