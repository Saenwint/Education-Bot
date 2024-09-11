from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, KeyboardButton, InlineKeyboardButton

start_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📋 Расписание"),
            KeyboardButton(text="🐍 Python")
        ],
        [
            #KeyboardButton(text="🗂 Заметки")
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
            KeyboardButton(text="1373"),
        ],
        [
            KeyboardButton(text="⬅️ Назад")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=False,
    input_field_placeholder="📋 Расписание"
)

timesheet_1373_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Четная 1373"),
            KeyboardButton(text="Нечетная 1373")
        ],
        [
            KeyboardButton(text="Текущая неделя 73"),
            KeyboardButton(text="Текущий день 73"),
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
            KeyboardButton(text="Текущая неделя 75"),
            KeyboardButton(text="Текущий день 75"),
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
            KeyboardButton(text="Текущая неделя 76"),
            KeyboardButton(text="Текущий день 76"),

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
            KeyboardButton(text="🎓 Курсы"),
            KeyboardButton(text="📚 Материалы")
        ],
        [
            KeyboardButton(text="⬅️ Назад")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=False,
    input_field_placeholder="🐍 Python"
)
# ADMIN MENU
admin_main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📋 Расписание"),
            KeyboardButton(text="🐍 Python")
        ],
        [
            #KeyboardButton(text="🗂 Заметки"),
            KeyboardButton(text="💻 Admin панель")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=False,
    input_field_placeholder="Меню"
)

admin_panel_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📋 Поправить расписание"),
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

admin_timesheet_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Добавить расписание"),
            KeyboardButton(text="Удалить расписание")
        ],
        [
            KeyboardButton(text="Изменить расписание"),
            KeyboardButton(text="All info расписание"),
        ],
        [
            KeyboardButton(text="⬅️ Go back")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=False,
    input_field_placeholder="📋 Расписание"
)

admin_py_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🎓 Поправить курсы"),
            KeyboardButton(text="📚 Поправить материалы")
        ],
        [
            KeyboardButton(text="⬅️ Go back")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=False,
    input_field_placeholder="🐍 Python"
)

admin_courses_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Добавить курсы"),
            KeyboardButton(text="Удалить курс")
        ],
        [
            KeyboardButton(text="All info курсы"),
            KeyboardButton(text="⬅️ Go back")

        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=False,
    input_field_placeholder="🐍 Python"
)


admin_materials_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Добавить материалы"),
            KeyboardButton(text="Удалить материал")
        ],
        [
            KeyboardButton(text="All info материалы"),
            KeyboardButton(text="⬅️ Go back")

        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=False,
    input_field_placeholder="🐍 Python"
)