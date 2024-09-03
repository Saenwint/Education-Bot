from datetime import datetime
from sqlalchemy.ext.asyncio import AsyncSession
from timesheet.models import Timesheet

from sqlalchemy import delete, select, update

day_to_weekday = {
    1: "Понедельник",
    2: "Вторник",
    3: "Среда",
    4: "Четверг",
    5: "Пятница",
    6: "Суббота",
}

async def get_even_timesheet_1375(session: AsyncSession):
    query = select(Timesheet).where(Timesheet.group == 1375, Timesheet.week == 0).order_by(Timesheet.day)
    result = await session.execute(query)
    timesheets = result.scalars().all()

    for timesheet in timesheets:
        timesheet.day = day_to_weekday.get(timesheet.day, "Неизвестный день")

    return timesheets


async def get_noteven_timesheet_1375(session: AsyncSession):
    query = select(Timesheet).where(Timesheet.group == 1375, Timesheet.week == 1).order_by(Timesheet.day)
    result = await session.execute(query)
    timesheets = result.scalars().all()

    for timesheet in timesheets:
        timesheet.day = day_to_weekday.get(timesheet.day, "Неизвестный день")

    return timesheets

async def get_even_timesheet_1376(session: AsyncSession):
    query = select(Timesheet).where(Timesheet.group == 1376, Timesheet.week == 0).order_by(Timesheet.day)
    result = await session.execute(query)
    timesheets = result.scalars().all()

    for timesheet in timesheets:
        timesheet.day = day_to_weekday.get(timesheet.day, "Неизвестный день")

    return timesheets

async def get_noteven_timesheet_1376(session: AsyncSession):
    query = select(Timesheet).where(Timesheet.group == 1376, Timesheet.week == 1).order_by(Timesheet.day)
    result = await session.execute(query)
    timesheets = result.scalars().all()

    for timesheet in timesheets:
        timesheet.day = day_to_weekday.get(timesheet.day, "Неизвестный день")

    return timesheets


async def update_timesheet(session: AsyncSession, timesheet_id: int, data):
    time_obj = datetime.strptime(data["time"], '%H:%M').time()

    query = update(Timesheet).where(Timesheet.id == timesheet_id).values(
        group=int(data["group"]),
        day=int(data["day"]),
        week=int(data["week"]),
        time=time_obj,
        cabinet=int(data["cabinet"]),
        subject=data["subject"],
        teacher=data["teacher"],
    )
    await session.execute(query)
    await session.commit()

async def delete_timesheet(session: AsyncSession, timesheet_id: int):
    result = await session.execute(select(Timesheet).where(Timesheet.id == timesheet_id))
    course = result.scalar_one_or_none()

    if course is None:
        return False  # Курс не найден

    # Если курс найден, удаляем его
    query = delete(Timesheet).where(Timesheet.id == timesheet_id)
    await session.execute(query)
    await session.commit()
    return True  # Курс удален


async def get_all_info(session: AsyncSession):
    query = select(Timesheet).order_by(Timesheet.day, Timesheet.group)
    result = await session.execute(query)
    timesheets = result.scalars().all()

    for timesheet in timesheets:
        timesheet.day = day_to_weekday.get(timesheet.day, "Неизвестный день")

    return timesheets