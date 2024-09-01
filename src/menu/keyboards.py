from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, KeyboardButton, InlineKeyboardButton

start_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📋 Расписание"),
            KeyboardButton(text="🐍 Python")
        ],
        [
            KeyboardButton(text="🗂 Заметки")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=False,
    input_field_placeholder="Меню"
)

timesheet_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="1375"),
            KeyboardButton(text="1376")
        ],
        [
            KeyboardButton(text="⬅️ Назад")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=False,
    input_field_placeholder="📋 Расписание"
)

timesheet_1375_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Четная 1375"),
            KeyboardButton(text="Нечетная 1375")
        ],
        [
            KeyboardButton(text="⬅️ Назад")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=False,
    input_field_placeholder="📋 Расписание"
)

timesheet_1376_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Четная 1376"),
            KeyboardButton(text="Нечетная 1376")
        ],
        [
            KeyboardButton(text="⬅️ Назад")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=False,
    input_field_placeholder="📋 Расписание"
)

py_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Курсы"),
            KeyboardButton(text="Материалы")
        ],
        [
            KeyboardButton(text="⬅️ Назад")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=False,
    input_field_placeholder="🐍 Python"
)

admin_main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📋 Расписание"),
            KeyboardButton(text="🐍 Python")
        ],
        [
            KeyboardButton(text="🗂 Заметки"),
            KeyboardButton(text="Admin панель")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=False,
    input_field_placeholder="Меню"
)

admin_panel_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📋 Добавить расписание"),
            KeyboardButton(text="🐍 Поправить python")
        ],
        [
            KeyboardButton(text="⬅️ Go back")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=False,
    input_field_placeholder="Меню"
)

admin_py_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Изменить курсы"),
            KeyboardButton(text="Изменить материалы")
        ],
        [
            KeyboardButton(text="⬅️ Go back")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=False,
    input_field_placeholder="🐍 Python"
)