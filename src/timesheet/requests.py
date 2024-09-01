from sqlalchemy.ext.asyncio import AsyncSession
from timesheet.models import Timesheet

from sqlalchemy import select

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


