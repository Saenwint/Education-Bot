from aiogram.utils.formatting import (
    Bold, as_list, as_marked_section, as_key_value, HashTag
)
from datetime import datetime

from aiogram import F, html, md
from aiogram.types import Message
from aiogram.filters import Command, CommandStart, CommandObject
from aiogram import Dispatcher, types

import menu.keyboards as kb

dp = Dispatcher()

# -----------Меню-----------

@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer("Выберите команду: ", reply_markup=kb.start_menu)


@dp.message(F.text == "Назад")
async def go_back(message: Message):
    await message.answer(f"Выберите команду: ", reply_markup=kb.start_menu)


@dp.message(F.text == "Расписание")
async def show_timesheet(message: Message):
    await message.answer(f"Выбирите группу: ", reply_markup=kb.sub_menu)


@dp.message(F.text == "1375")
async def show_timesheet(message: Message):
    await message.answer(f"Расписание для группы 1375: ")


@dp.message(F.text == "1376")
async def show_timesheet(message: Message):
    await message.answer(f"Расписание для группы 1376: ")


@dp.message(F.text == "Заметки")
async def show_notes(message: Message):
    await message.answer(f"Ваши заметки: ")


@dp.message(F.text == "Python")
async def show_timesheet(message: Message):
    await message.answer(f"Выбирите действие: ", reply_markup=kb.py_menu)


@dp.message(F.text == "Курсы")
async def show_timesheet(message: Message):
    await message.answer(f"Все добавленные курсы по Python: ")


@dp.message(F.text == "Материалы")
async def show_timesheet(message: Message):
    await message.answer(f"Все добавленные материалы по Python: ")


# ------------------------
# Если не указать фильтр F.text, 
# то хэндлер сработает даже на картинку с подписью /test
@dp.message(F.text, Command("test"))
async def any_message(message: Message):
    await message.answer(
        "Hello, *world*!", 
    )


@dp.message(Command("hello"))
async def cmd_hello(message: Message):
    await message.answer(
        f"Hello, *{message.from_user.full_name}*",
    )


