from sqlalchemy.ext.asyncio import AsyncSession
from materials.models import Materials, Courses

from sqlalchemy import delete, select

async def get_courses(session: AsyncSession):
    query = select(Courses)
    result = await session.execute(query)
    return result.scalars().all()


async def delete_courses(session: AsyncSession, courses_id: int):
    result = await session.execute(select(Courses).where(Courses.id == courses_id))
    course = result.scalar_one_or_none()

    if course is None:
        return False  # Курс не найден

    # Если курс найден, удаляем его
    query = delete(Courses).where(Courses.id == courses_id)
    await session.execute(query)
    await session.commit()
    return True  # Курс удален


async def get_materials(session: AsyncSession):
    query = select(Materials)
    result = await session.execute(query)
    return result.scalars().all()


async def delete_materials(session: AsyncSession, materials_id: int):
    result = await session.execute(select(Materials).where(Materials.id == materials_id))
    course = result.scalar_one_or_none()

    if course is None:
        return False  # Курс не найден

    # Если курс найден, удаляем его
    query = delete(Materials).where(Materials.id == materials_id)
    await session.execute(query)
    await session.commit()
    return True  # Курс удален

