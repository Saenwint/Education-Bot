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

@user_router.message(F.text == "1373")
async def show_timesheet_1373(message: Message):
    await message.answer("Выберете неделю", reply_markup=kb.timesheet_1373_menu)


@user_router.message(F.text == "Четная 1373")
async def show_even_timesheet_1373(message: Message, session: AsyncSession):
    timesheets = await tm_request.get_even_timesheet_1373(session)

    if not timesheets:
        await message.answer("Расписание еще не добавлено 😔")
    else:
        weekly_schedule = {}

        time_format = "%H:%M"

        await message.answer("Расписание четной недели 1373")

        for timesheet in timesheets:
            if timesheet.day not in weekly_schedule:
                weekly_schedule[timesheet.day] = []
            weekly_schedule[timesheet.day].append(f"<pre>Время: {timesheet.time_start.strftime(time_format)} - {timesheet.time_end.strftime(time_format)}\nПредмет: {timesheet.subject} Кабинет: {timesheet.cabinet}\nПреподаватель: {timesheet.teacher}</pre>")
        
        for day, schedule in weekly_schedule.items():
            #full = "<pre>" + "\n".join(schedule) +"</pre>"
            await message.answer((f"<b>{day}</b>\n" + "\n".join(schedule)))
        


@user_router.message(F.text == "Нечетная 1373")
async def show_noteven_timesheet_1373(message: Message, session: AsyncSession):
    timesheets = await tm_request.get_noteven_timesheet_1373(session)
    
    if not timesheets:
        await message.answer("Расписание еще не добавлено 😔")
    else:
        weekly_schedule = {}

        time_format = "%H:%M"

        await message.answer("Расписание нечетной недели 1373")

        for timesheet in timesheets:
            if timesheet.day not in weekly_schedule:
                weekly_schedule[timesheet.day] = []
            weekly_schedule[timesheet.day].append(f"<pre>Время: {timesheet.time_start.strftime(time_format)} - {timesheet.time_end.strftime(time_format)}\nПредмет: {timesheet.subject} Кабинет: {timesheet.cabinet}\nПреподаватель: {timesheet.teacher}</pre>")
        
        for day, schedule in weekly_schedule.items():
            #full = "<pre>" + "\n".join(schedule) +"</pre>"
            await message.answer((f"<b>{day}</b>\n" + "\n".join(schedule)))


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

        time_format = "%H:%M"

        await message.answer("Расписание четной недели 1375")

        for timesheet in timesheets:
            if timesheet.day not in weekly_schedule:
                weekly_schedule[timesheet.day] = []
            weekly_schedule[timesheet.day].append(f"<pre>Время: {timesheet.time_start.strftime(time_format)} - {timesheet.time_end.strftime(time_format)}\nПредмет: {timesheet.subject} Кабинет: {timesheet.cabinet}\nПреподаватель: {timesheet.teacher}</pre>")
        
        for day, schedule in weekly_schedule.items():
            #full = "<pre>" + "\n".join(schedule) +"</pre>"
            await message.answer((f"<b>{day}</b>\n" + "\n".join(schedule)))
        


@user_router.message(F.text == "Нечетная 1375")
async def show_noteven_timesheet_1375(message: Message, session: AsyncSession):
    timesheets = await tm_request.get_noteven_timesheet_1375(session)
    
    if not timesheets:
        await message.answer("Расписание еще не добавлено 😔")
    else:
        weekly_schedule = {}

        time_format = "%H:%M"

        await message.answer("Расписание нечетной недели 1375")

        for timesheet in timesheets:
            if timesheet.day not in weekly_schedule:
                weekly_schedule[timesheet.day] = []
            weekly_schedule[timesheet.day].append(f"<pre>Время: {timesheet.time_start.strftime(time_format)} - {timesheet.time_end.strftime(time_format)}\nПредмет: {timesheet.subject} Кабинет: {timesheet.cabinet}\nПреподаватель: {timesheet.teacher}</pre>")
        
        for day, schedule in weekly_schedule.items():
            #full = "<pre>" + "\n".join(schedule) +"</pre>"
            await message.answer((f"<b>{day}</b>\n" + "\n".join(schedule)))


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

        time_format = "%H:%M"

        await message.answer("Расписание четной недели 1376")

        for timesheet in timesheets:
            if timesheet.day not in weekly_schedule:
                weekly_schedule[timesheet.day] = []
            weekly_schedule[timesheet.day].append(f"<pre>Время: {timesheet.time_start.strftime(time_format)} - {timesheet.time_end.strftime(time_format)}\nПредмет: {timesheet.subject} Кабинет: {timesheet.cabinet}\nПреподаватель: {timesheet.teacher}</pre>")
        
        for day, schedule in weekly_schedule.items():
            #full = "<pre>" + "\n".join(schedule) +"</pre>"
            await message.answer((f"<b>{day}</b>\n" + "\n".join(schedule)))


@user_router.message(F.text == "Нечетная 1376")
async def show_noteven_timesheet_1376(message: Message, session: AsyncSession):
    timesheets = await tm_request.get_noteven_timesheet_1376(session)

    if not timesheets:
        await message.answer("Расписание еще не добавлено 😔")
    else:       
        weekly_schedule = {}

        time_format = "%H:%M"

        await message.answer("Расписание нечетной недели 1376")

        for timesheet in timesheets:
            if timesheet.day not in weekly_schedule:
                weekly_schedule[timesheet.day] = []
            weekly_schedule[timesheet.day].append(f"<pre>Время: {timesheet.time_start.strftime(time_format)} - {timesheet.time_end.strftime(time_format)}\nПредмет: {timesheet.subject} Кабинет: {timesheet.cabinet}\nПреподаватель: {timesheet.teacher}</pre>")
        
        for day, schedule in weekly_schedule.items():
            #full = "<pre>" + "\n".join(schedule) +"</pre>"
            await message.answer((f"<b>{day}</b>\n" + "\n".join(schedule)))

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
            response += f"<a href='{course.link}'>{course.description}</a>\n"
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
            response += f"<a href='{material.link}'>{material.description}</a>\n"
        await message.answer(response)


