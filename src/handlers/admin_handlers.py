from datetime import datetime
from aiogram import Router, types, F
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from database import session_maker
from timesheet.models import Timesheet
from sqlalchemy.ext.asyncio import AsyncSession

from filters.chat_types import IsAdmin
from config import config
import menu.keyboards as kb
import user.requests as user_request
import timesheet.requests as tm_request
from database import session_maker


admin_router = Router()
admin_router.message.filter(IsAdmin())

@admin_router.message(CommandStart())
async def start_admin_cmd(message: types.Message):
    await user_request.set_user(message.from_user.id, message.from_user.username)

    if message.from_user.id == config.ADMIN:
        await message.answer("Добро пожаловать, создатель", reply_markup=kb.admin_main_menu)
    else:
        await message.answer("Добро пожаловать", reply_markup=kb.start_menu)
    

@admin_router.message(F.text == "Admin панель")
async def get_admin_panel(message: types.Message):
    await message.answer("Вы вошли в админ панель", reply_markup=kb.admin_panel_menu)


@admin_router.message(F.text == "⬅️ Go back")
async def go_back(message: types.Message):
    await message.answer("Выберите команду", reply_markup=kb.admin_main_menu)


@admin_router.message(F.text == "🐍 Поправить python")
async def edit_python(message: types.Message):
    await message.answer("Выбирите команду", reply_markup=kb.admin_py_menu)

# Добавление курсов
@admin_router.message(F.text == "Добавить курсы")
async def edit_courses(message: types.Message):
    await message.answer("Изменение курсов по Python")

# Добавление материалов
@admin_router.message(F.text == "Добавить материалы")
async def edit_materials(message: types.Message):
    await message.answer("Изменение материалов по Python")


# Добавление расписания
class AddTimesheet(StatesGroup):
    group = State()
    day = State()
    week = State()
    time = State()
    cabinet = State()
    subject = State()
    teacher = State()

@admin_router.message(StateFilter(None), F.text == "📋 Добавить расписание")
async def add_group(message: types.Message, state: FSMContext):
    await message.answer(f"Введите группу", reply_markup=types.ReplyKeyboardRemove())
    await state.set_state(AddTimesheet.group)


@admin_router.message(AddTimesheet.group, F.text)
async def add_day(message: types.Message, state: FSMContext):
    await state.update_data(group=message.text)
    await message.answer(f"Введите день")
    await state.set_state(AddTimesheet.day)


@admin_router.message(AddTimesheet.day, F.text)
async def add_week(message: types.Message, state: FSMContext):
    await state.update_data(day=message.text)
    await message.answer(f"Введите неделю")
    await state.set_state(AddTimesheet.week)


@admin_router.message(AddTimesheet.week, F.text)
async def add_time(message: types.Message, state: FSMContext):
    await state.update_data(week=message.text)
    await message.answer(f"Введите время")
    await state.set_state(AddTimesheet.time)


@admin_router.message(AddTimesheet.time, F.text)
async def add_cabinet(message: types.Message, state: FSMContext):
    await state.update_data(time=message.text)
    await message.answer(f"Введите кабинет")
    await state.set_state(AddTimesheet.cabinet)


@admin_router.message(AddTimesheet.cabinet, F.text)
async def add_subject(message: types.Message, state: FSMContext):
    await state.update_data(cabinet=message.text)
    await message.answer(f"Введите предмет")
    await state.set_state(AddTimesheet.subject)


@admin_router.message(AddTimesheet.subject, F.text)
async def add_teacher(message: types.Message, state: FSMContext):
    await state.update_data(subject=message.text)
    await message.answer(f"Введите преподавателя")
    await state.set_state(AddTimesheet.teacher)


@admin_router.message(AddTimesheet.teacher, F.text)
async def add_timesheet(message: types.Message, state: FSMContext, session: AsyncSession):
    await state.update_data(teacher=message.text)
    await message.answer(f"Добавлено", reply_markup=kb.admin_main_menu)
    data = await state.get_data()

    time_obj = datetime.strptime(data["time"], '%H:%M').time()
    obj = Timesheet(
        group=int(data["group"]),
        day=int(data["day"]),
        week=int(data["week"]),
        time=time_obj,
        cabinet=int(data["cabinet"]),
        subject=data["subject"],
        teacher=data["teacher"],
    )

    session.add(obj)
    await session.commit()
    await message.answer(str(data))
    await state.clear()

