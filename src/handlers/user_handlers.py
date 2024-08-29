from aiogram.utils.formatting import (
    Bold, as_list, as_marked_section, as_key_value, HashTag
)
from aiogram import F, md, Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart, CommandObject
from aiogram import types
from datetime import datetime

from config import config
import menu.keyboards as kb
import user.requests as request

user_router = Router()

#=============================-Меню-=============================

@user_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await request.set_user(message.from_user.id, message.from_user.full_name)
    await message.answer("Добро пожаловать\\!", reply_markup=kb.start_menu)


@user_router.message(F.text == "⬅️ Назад")
async def go_back(message: Message):
    if message.from_user.id == config.ADMIN:
        await message.answer("Выберите команду", reply_markup=kb.admin_menu_main)
    else:
        await message.answer("Выберите команду", reply_markup=kb.start_menu)


@user_router.message(F.text == "📋 Расписание")
async def show_timesheet(message: Message):
    await message.answer(f"Выбирите группу", reply_markup=kb.sub_menu)


@user_router.message(F.text == "1375")
async def show_timesheet(message: Message):
    await message.answer(f"Расписание для группы 1375: ")


@user_router.message(F.text == "1376")
async def show_timesheet(message: Message):
    await message.answer(f"Расписание для группы 1376: ")


@user_router.message(F.text.in_({'🗂 Заметки', 'заметки', 'Заметки', 'notes'}) )
async def show_notes(message: Message):
    await message.answer(f"В разработке")


@user_router.message(F.text == "🐍 Python")
async def show_timesheet(message: Message):
    await message.answer(f"Выбирите команду", reply_markup=kb.py_menu)


@user_router.message(F.text == "Курсы")
async def show_timesheet(message: Message):
    await message.answer(f"Все добавленные курсы по Python: ")


@user_router.message(F.text == "Материалы")
async def show_timesheet(message: Message):
    await message.answer(f"Все добавленные материалы по Python: ")

#=============================--=============================
# Если не указать фильтр F.text, 
# то хэндлер сработает даже на картинку с подписью /test
@user_router.message(F.text, Command("test"))
async def any_message(message: Message):
    await message.answer(
        "Hello, *world*\\!", 
    )


@user_router.message(F.text, Command("hello"))
async def cmd_hello(message: Message):
    await message.answer(
        f"Hello, *{message.from_user.full_name}*",
    )


