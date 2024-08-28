from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, KeyboardButton, InlineKeyboardButton

start_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Расписание"),
            KeyboardButton(text="Python")
        ],
        [
            KeyboardButton(text="Заметки")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=False,
    input_field_placeholder="Меню"
)

sub_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="1375"),
            KeyboardButton(text="1376")
        ],
        [
            KeyboardButton(text="Назад")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=False,
    input_field_placeholder="Расписание"
)

py_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Курсы"),
            KeyboardButton(text="Материалы")
        ],
        [
            KeyboardButton(text="Назад")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=False,
    input_field_placeholder="Python"
)