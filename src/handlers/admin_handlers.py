from aiogram import Router, types, F
from aiogram.filters import Command, CommandStart

from filters.chat_types import IsAdmin
from config import config
import menu.keyboards as kb
import user.requests as request


admin_router = Router()
admin_router.message.filter(IsAdmin())

@admin_router.message(CommandStart())
async def start_admin_cmd(message: types.Message):
    await request.set_user(message.from_user.id, message.from_user.full_name)

    if message.from_user.id == config.ADMIN:
        await message.answer(f"Добро пожаловать, создатель\\!", reply_markup=kb.admin_menu_main)
    else:
        await message.answer("Добро пожаловать\\!", reply_markup=kb.start_menu)
    

@admin_router.message(F.text == "Admin панель")
async def start_admin_cmd(message: types.Message):
    await message.answer("Вы вошли в админ панель", reply_markup=kb.admin_panel_menu)


@admin_router.message(F.text == "⬅️ Go back")
async def go_back(message: types.Message):
    await message.answer(f"Выберите команду", reply_markup=kb.admin_menu_main)


@admin_router.message(F.text == "📋 Изменить расписание")
async def show_timesheet(message: types.Message):
    await message.answer(f"Выбирите группу", reply_markup=kb.admin_menu_timesheet)


@admin_router.message(F.text == "Изменить для 1375")
async def show_timesheet(message: types.Message):
    await message.answer(f"Внесите изменения для группы 1375: ")


@admin_router.message(F.text == "Изменить для 1376")
async def show_timesheet(message: types.Message):
    await message.answer(f"Внесите изменения для группы 1376: ")


@admin_router.message(F.text == "🐍 Поправить python")
async def show_timesheet(message: types.Message):
    await message.answer(f"Выбирите команду", reply_markup=kb.admin_menu_py)


@admin_router.message(F.text == "Изменить курсы")
async def show_timesheet(message: types.Message):
    await message.answer(f"Изменение курсов по Python: ")


@admin_router.message(F.text == "Изменить материалы")
async def show_timesheet(message: types.Message):
    await message.answer(f"Изменение материалов по Python: ")