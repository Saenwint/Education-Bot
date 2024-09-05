from aiogram import F, md, Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart, CommandObject
from aiogram import types
from datetime import datetime
from sqlalchemy.ext.asyncio import AsyncSession
from aiogram.enums import ParseMode


from config import config
import menu.keyboards as kb
import user.requests as us_request
import timesheet.requests as tm_request
import materials.requests as m_request

user_router = Router()

#=============================-Меню-=============================

@user_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await us_request.set_user(str(message.from_user.id), message.from_user.full_name)
    await message.answer("Добро пожаловать 🤓", reply_markup=kb.start_menu)


@user_router.message(F.text == "⬅️ Назад")
async def go_back(message: Message):
    if message.from_user.id == config.ADMIN:
        await message.answer("Выберете команду", reply_markup=kb.admin_main_menu)
    else:
        await message.answer("Выберете команду", reply_markup=kb.start_menu)

# ==================Timesheet==================

@user_router.message(F.text == "📋 Расписание")
async def show_timesheet(message: Message):
    await message.answer("Выберете группу", reply_markup=kb.timesheet_menu)


@user_router.message(F.text == "1375")
async def show_timesheet_1375(message: Message):
    await message.answer("Выберете неделю", reply_markup=kb.timesheet_1375_menu)


@user_router.message(F.text == "Четная 1375")
async def show_even_timesheet_1375(message: Message, session: AsyncSession):
    timesheets = await tm_request.get_even_timesheet_1375(session)

    if not timesheets:
        await message.answer("Расписание еще не добавлено 😔")
    else:
        weekly_schedule = {}

        for timesheet in timesheets:
            if timesheet.day not in weekly_schedule:
                weekly_schedule[timesheet.day] = []
            weekly_schedule[timesheet.day].append(f"<b>{timesheet.time_start} - {timesheet.time_end}</b>\n<b>{timesheet.subject}</b> <u>{timesheet.teacher}</u>\n{timesheet.cabinet}")
        
        for day, schedule in weekly_schedule.items():
            await message.answer((f"--- {day} ---\n" + "\n".join(schedule)))
        
        await message.answer("Расписание четной недели 1375")


@user_router.message(F.text == "Нечетная 1375")
async def show_noteven_timesheet_1375(message: Message, session: AsyncSession):
    timesheets = await tm_request.get_noteven_timesheet_1375(session)
    
    if not timesheets:
        await message.answer("Расписание еще не добавлено 😔")
    else:
        weekly_schedule = {}

        for timesheet in timesheets:
            if timesheet.day not in weekly_schedule:
                weekly_schedule[timesheet.day] = []
            weekly_schedule[timesheet.day].append(f"<b>{timesheet.time_start} - {timesheet.time_end}</b>\n<b>{timesheet.subject}</b> <u>{timesheet.teacher}</u>\n{timesheet.cabinet}")
        
        for day, schedule in weekly_schedule.items():
            await message.answer((f"--- {day} ---\n" + "\n".join(schedule)))
        
        await message.answer("Расписание нечетной недели 1375")


@user_router.message(F.text == "1376")
async def show_timesheet_1376(message: Message):
    await message.answer("Выберете неделю", reply_markup=kb.timesheet_1376_menu)


@user_router.message(F.text == "Четная 1376")
async def show_even_timesheet_1376(message: Message, session: AsyncSession):
    timesheets = await tm_request.get_even_timesheet_1376(session)

    if not timesheets:
        await message.answer("Расписание еще не добавлено 😔")
    else:
        weekly_schedule = {}

        for timesheet in timesheets:
            if timesheet.day not in weekly_schedule:
                weekly_schedule[timesheet.day] = []
            weekly_schedule[timesheet.day].append(f"<b>{timesheet.time_start} - {timesheet.time_end}</b>\n<b>{timesheet.subject}</b> <u>{timesheet.teacher}</u>\n{timesheet.cabinet}")
        
        for day, schedule in weekly_schedule.items():
            await message.answer((f"--- {day} ---\n" + "\n".join(schedule)))
        
        await message.answer("Расписание четной недели 1376")


@user_router.message(F.text == "Нечетная 1376")
async def show_noteven_timesheet_1376(message: Message, session: AsyncSession):
    timesheets = await tm_request.get_noteven_timesheet_1376(session)

    if not timesheets:
        await message.answer("Расписание еще не добавлено 😔")
    else:       
        weekly_schedule = {}

        for timesheet in timesheets:
            if timesheet.day not in weekly_schedule:
                weekly_schedule[timesheet.day] = []
            weekly_schedule[timesheet.day].append(f"<b>{timesheet.time_start} - {timesheet.time_end}</b>\n<b>{timesheet.subject}</b> <u>{timesheet.teacher}</u>\n{timesheet.cabinet}")
        
        for day, schedule in weekly_schedule.items():
            await message.answer((f"--- {day} ---\n" + "\n".join(schedule)))
        
        await message.answer("Расписание нечетной недели 1376")

# ==================Notes==================

@user_router.message(F.text == '🗂 Заметки')
async def show_notes(message: Message):
    await message.answer(f"В разработке")

# ==================Python==================

@user_router.message(F.text == "🐍 Python")
async def show_python(message: Message):
    await message.answer(f"Выберете команду", reply_markup=kb.py_menu)

# ==================Courses==================

@user_router.message(F.text == "🎓 Курсы")
async def show_python_courses(message: Message, session: AsyncSession):
    courses = await m_request.get_courses(session)

    if not courses:
        await message.answer("Курсы еще не добавлены 😔")
    else:
        await message.answer("Все курсы по Python")
        response = ""
        for course in courses:
            response += f"{course.description} - {course.link}\n"
        await message.answer(response)

# ==================Materials==================

@user_router.message(F.text == "📚 Материалы")
async def show_python_materials(message: Message, session: AsyncSession):
    materials = await m_request.get_materials(session)

    if not materials:
        await message.answer("Материалы еще не добавлены 😔")
    else:
        await message.answer("Все материалы по Python")
        response = ""
        for material in materials:
            response += f"{material.description} - {material.link}\n"
        await message.answer(response)


