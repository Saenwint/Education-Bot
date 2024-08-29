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

sub_menu = ReplyKeyboardMarkup(
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

admin_menu_main = ReplyKeyboardMarkup(
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
            KeyboardButton(text="📋 Изменить расписание"),
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
admin_menu_timesheet = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Изменить для 1375"),
            KeyboardButton(text="Изменить для 1376")
        ],
        [
            KeyboardButton(text="⬅️ Go back")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=False,
    input_field_placeholder="📋 Расписание"
)

admin_menu_py = ReplyKeyboardMarkup(
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