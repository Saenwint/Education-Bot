from datetime import datetime
from aiogram import Router, types, F
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from materials.models import Courses, Materials
from timesheet.models import Timesheet
from sqlalchemy.ext.asyncio import AsyncSession
from aiogram.enums import ParseMode

from filters.chat_types import IsAdmin
from config import config
import menu.keyboards as kb
import user.requests as user_request
import timesheet.requests as tm_request
import materials.requests as m_request

admin_router = Router()
admin_router.message.filter(IsAdmin())

# Стартовая команда(добавить меню для нее)
@admin_router.message(CommandStart())
async def start_admin_cmd(message: types.Message):
    await user_request.set_user(str(message.from_user.id), message.from_user.username)

    if message.from_user.id == config.ADMIN:
        await message.answer("Добро пожаловать, создатель 🥳", reply_markup=kb.admin_main_menu)
    else:
        await message.answer("Добро пожаловать 🤓", reply_markup=kb.start_menu)
    
# Панель админа
@admin_router.message(F.text == "💻 Admin панель")
async def get_admin_panel(message: types.Message):
    await message.answer("Вы вошли в админ панель", reply_markup=kb.admin_panel_menu)


@admin_router.message(F.text == "⬅️ Go back")
async def go_back(message: types.Message):
    await message.answer("Выберите команду", reply_markup=kb.admin_main_menu)


@admin_router.message(F.text == "🐍 Поправить python")
async def edit_python(message: types.Message):
    await message.answer("Выбирите команду", reply_markup=kb.admin_py_menu)


# ==================Courses==================

@admin_router.message(F.text == "🎓 Поправить курсы")
async def edit_courses(message: types.Message):
    await message.answer("Выбирите команду", reply_markup=kb.admin_courses_menu)

# Добавление курсов
class AddCourses(StatesGroup):
    description = State()
    link = State()

@admin_router.message(StateFilter(None), F.text == "Добавить курсы")
async def add_courses(message: types.Message, state: FSMContext):
    await message.answer(f"Введите описание", reply_markup=types.ReplyKeyboardRemove())
    await state.set_state(AddCourses.description)


@admin_router.message(AddCourses.description, F.text)
async def add_description(message: types.Message, state: FSMContext):
    await state.update_data(description=message.text)
    await message.answer(f"Введите ссылку")
    await state.set_state(AddCourses.link)

@admin_router.message(AddCourses.link, F.text)
async def add_link(message: types.Message, state: FSMContext, session: AsyncSession):
    await state.update_data(link=message.text)
    await message.answer(f"✅ Добавлено", reply_markup=kb.admin_panel_menu)
    data = await state.get_data()
    format_data = ", ".join([f"{key}: {value}" for key, value in data.items()])

    obj = Courses(
        description=data["description"],
        link=data["link"]
    )

    session.add(obj)
    await session.commit()
    await message.answer(format_data)
    await state.clear()

# Удаление курсов
class DeleteCourses(StatesGroup):
    id = State()


@admin_router.message(StateFilter(None), F.text == "Удалить курс")
async def delete_courses_by_id(message: types.Message, state: FSMContext):

    await message.answer(f"Введите id курса", reply_markup=types.ReplyKeyboardRemove())
    await state.set_state(DeleteCourses.id)


@admin_router.message(DeleteCourses.id, F.text)
async def delete_courses(message: types.Message, state: FSMContext, session: AsyncSession):
    
    if message.text.isnumeric() == False:
        await message.answer(f"❗️Введите корректный ID")
    else:
        courses_id = int(message.text)
        deleted = await m_request.delete_courses(session, courses_id)
        if deleted:
            await message.answer(f"✅ Курс с ID {courses_id} удален.", reply_markup=kb.admin_panel_menu)
        else:
            await message.answer(f"❌ Курс с ID {courses_id} не найден.", reply_markup=kb.admin_courses_menu)

        await state.clear()

# Получение всей информации
@admin_router.message(F.text == "All info курсы")
async def courses_info(message: types.Message, session: AsyncSession):
    courses = await m_request.get_courses(session)

    if not courses:
        await message.answer("Курсы еще не добавлены 😔")
    else:
        await message.answer("Все курсы по Python")
        response = ""
        for course in courses:
            response += f"ID: {course.id}; INFO: {course.description[:16]}... - {course.link}\n"
        await message.answer(response)
    

# ==================Materials==================

@admin_router.message(F.text == "📚 Поправить материалы")
async def edit_materials(message: types.Message):
    await message.answer("Выбирите команду", reply_markup=kb.admin_materials_menu)

# Добавление материалов
class AddMaterials(StatesGroup):
    description = State()
    link = State()
    

@admin_router.message(StateFilter(None), F.text == "Добавить материалы")
async def add_materials(message: types.Message, state: FSMContext):
    await message.answer(f"Введите описание", reply_markup=types.ReplyKeyboardRemove())
    await state.set_state(AddMaterials.description)


@admin_router.message(AddMaterials.description, F.text)
async def add_description(message: types.Message, state: FSMContext):
    await state.update_data(description=message.text)
    await message.answer("Введите ссылку")
    await state.set_state(AddMaterials.link)


@admin_router.message(AddMaterials.link, F.text)
async def add_link(message: types.Message, state: FSMContext, session: AsyncSession):
    await state.update_data(link=message.text)
    await message.answer(f"✅ Добавлено", reply_markup=kb.admin_panel_menu)
    data = await state.get_data()
    format_data = ", ".join([f"{key}: {value}" for key, value in data.items()])

    obj = Materials(
        description=data["description"],
        link=data["link"]
    )

    session.add(obj)
    await session.commit()
    await message.answer(format_data)
    await state.clear()


# Удаление материалов
class DeleteMaterials(StatesGroup):
    id = State()


@admin_router.message(StateFilter(None), F.text == "Удалить материал")
async def delete_materials_by_id(message: types.Message, state: FSMContext):

    await message.answer(f"Введите id материала", reply_markup=types.ReplyKeyboardRemove())
    await state.set_state(DeleteMaterials.id)


@admin_router.message(DeleteMaterials.id, F.text)
async def delete_materials(message: types.Message, state: FSMContext, session: AsyncSession):
    if message.text.isnumeric() == False:
        await message.answer(f"❗️Введите корректный ID")
    else:
        materials_id = int(message.text)
        deleted = await m_request.delete_materials(session, materials_id)
        if deleted:
            await message.answer(f"✅ Материал с ID {materials_id} удален.", reply_markup=kb.admin_panel_menu)
        else:
            await message.answer(f"❌ Материал с ID {materials_id} не найден.", reply_markup=kb.admin_materials_menu)
        
        await state.clear()

# Получение всей информации
@admin_router.message(F.text == "All info материалы")
async def materials_info(message: types.Message, session: AsyncSession):
    materials = await m_request.get_materials(session)

    if not materials:
        await message.answer("Материалы еще не добавлены 😔")
    else:
        await message.answer("Все материалы по Python")
        response = ""
        for material in materials:
            response += f"ID: {material.id}; INFO: {material.description[:16]}... - {material.link}\n"
        await message.answer(response)

# ==================Timesheet==================escape_markdown

@admin_router.message(F.text == "📋 Поправить расписание")
async def edit_timesheet(message: types.Message):
    await message.answer("Выбирите команду", reply_markup=kb.admin_timesheet_menu)


# Добавление расписания
class AddTimesheet(StatesGroup):
    group = State()
    day = State()
    week = State()
    time_start = State()
    time_end = State()
    cabinet = State()
    subject = State()
    teacher = State()

    texts = {
        'AddTimesheet:group': 'Введите группу заново',
        'AddTimesheet:week': 'Введите тип недели заново',
        'AddTimesheet:day': 'Введите день недели заново',
        'AddTimesheet:time_start': 'Введите время начала заново',
        'AddTimesheet:time_end': 'Введите время конца заново',
        'AddTimesheet:cabinet': 'Введите кабинет заново',
        'AddTimesheet:subject': 'Введите предмет заново',
        'AddTimesheet:teacher': 'Введите преподавателя заново'
    }

@admin_router.message(StateFilter(None), F.text == "Добавить расписание")
async def add_group(message: types.Message, state: FSMContext):

    await message.answer(f"Введите группу", reply_markup=types.ReplyKeyboardRemove())
    await state.set_state(AddTimesheet.group)

@admin_router.message(StateFilter('*'), Command("отмена"))
@admin_router.message(StateFilter('*'), F.text.casefold() == "отмена")
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.clear()
    await message.answer("Действия отменены", reply_markup=kb.admin_main_menu)


@admin_router.message(StateFilter('*'), Command("назад"))
@admin_router.message(StateFilter('*'), F.text.casefold() == "назад")
async def get_back_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state == AddTimesheet.group:
        await message.answer("Предыдущего шага нет")
        return
    previous = None
    for step in AddTimesheet.__all_states__:
        if step.state == current_state:
            await state.set_state(previous)
            await message.answer(f"Вы вернулись к предыдущему шагу \n {AddTimesheet.texts[previous.state]}")
            return
        previous = step


@admin_router.message(AddTimesheet.group, F.text)
async def add_week(message: types.Message, state: FSMContext):
    if message.text not in ["1375", "1376"]:
        await message.answer(f"❗️Введите корректный номер группы")
    else:
        await state.update_data(group=message.text)
        await message.answer("Введите тип недели")
        await state.set_state(AddTimesheet.week)


@admin_router.message(AddTimesheet.week, F.text)
async def add_day(message: types.Message, state: FSMContext):
    if message.text not in ["0", "1"]:
        await message.answer("❗️Введите корректный тип недели 0 - чет, 1 - нечет")
    else:
        await state.update_data(week=message.text)
        await message.answer(f"Введите день недели")
        await state.set_state(AddTimesheet.day)


@admin_router.message(AddTimesheet.day, F.text)
async def add_time_start(message: types.Message, state: FSMContext):
    if (message.text not in ["1", "2", "3", "4", "5", "6"]):
        await message.answer(f"❗️Введите корректный день недели")
    else:
        await state.update_data(day=message.text)
        await message.answer(f"Введите время начала")
        await state.set_state(AddTimesheet.time_start)


@admin_router.message(AddTimesheet.time_start, F.text)
async def add_time_end(message: types.Message, state: FSMContext):
    await state.update_data(time_start=message.text)
    await message.answer(f"Введите время конца")
    await state.set_state(AddTimesheet.time_end)


@admin_router.message(AddTimesheet.time_end, F.text)
async def add_cabinet(message: types.Message, state: FSMContext):
    data = await state.get_data()
    time_start_str = data["time_start"]
    time_end_str = message.text

    time_format = "%H:%M"

    time_start = datetime.strptime(time_start_str, time_format)
    time_end = datetime.strptime(time_end_str, time_format)
    
    if time_start >= time_end:
        await state.update_data(time_start=None)
        await message.answer(f"❗️Время начала не может быть больше времени конца")
        await message.answer(f"Введите время начала заново")
        await state.set_state(AddTimesheet.time_start)
    else:
        await state.update_data(time_end=message.text)
        await message.answer(f"Введите кабинет")
        await state.set_state(AddTimesheet.cabinet)


@admin_router.message(AddTimesheet.cabinet, F.text)
async def add_subject(message: types.Message, state: FSMContext):
    if message.text.isnumeric() == False:
        await message.answer(f"❗️Введите корректный номер кабинета")
    else:
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
    await message.answer(f"✅ Добавлено", reply_markup=kb.admin_panel_menu)
    data = await state.get_data()
    format_data = ", ".join([f"{key}: {value}" for key, value in data.items()])

    time_start_obj = datetime.strptime(data["time_start"], '%H:%M').time()
    time_end_obj = datetime.strptime(data["time_end"], '%H:%M').time()
    obj = Timesheet(
        group=int(data["group"]),
        day=int(data["day"]),
        week=int(data["week"]),
        time_start=time_start_obj,
        time_end=time_end_obj,
        cabinet=int(data["cabinet"]),
        subject=data["subject"],
        teacher=data["teacher"],
    )

    session.add(obj)
    await session.commit()
    await message.answer(format_data)
    await state.clear()


class DeleteTimesheet(StatesGroup):
    id = State()


@admin_router.message(StateFilter(None), F.text == "Удалить расписание")
async def delete_timesheet_by_id(message: types.Message, state: FSMContext):

    await message.answer(f"Введите id расписания", reply_markup=types.ReplyKeyboardRemove())
    await state.set_state(DeleteTimesheet.id)


@admin_router.message(DeleteTimesheet.id, F.text)
async def delete_timesheet(message: types.Message, state: FSMContext, session: AsyncSession):
    if message.text.isnumeric() == False:
        await message.answer(f"❗️Введите корректный ID")
    else:
        timesheet_id = int(message.text)
        deleted = await tm_request.delete_timesheet(session, timesheet_id)
        if deleted:
            await message.answer(f"✅ Расписание с ID {timesheet_id} удалено.", reply_markup=kb.admin_panel_menu)
        else:
            await message.answer(f"❌ Расписание с ID {timesheet_id} не найдено.", reply_markup=kb.admin_timesheet_menu)
        await state.clear()

# Получение всей информации
@admin_router.message(F.text == "All info расписание")
async def timesheet_info(message: types.Message, session: AsyncSession):
    timesheets = await tm_request.get_all_info(session)

    if not timesheets:
        await message.answer("Расписание еще не добавлено 😔")
    else:
        await message.answer("Всё Расписание")
        weekly_schedule = {}

        for timesheet in timesheets:
            if timesheet.day not in weekly_schedule:
                weekly_schedule[timesheet.day] = []
            weekly_schedule[timesheet.day].append(f"ID: {timesheet.id}; INFO: {timesheet.group}, {timesheet.week}, {timesheet.time_start}, {timesheet.time_end}, {timesheet.cabinet}, {timesheet.subject}, {timesheet.teacher}")
        
        for day, schedule in weekly_schedule.items():
            await message.answer(f"--- {day} ---\n" + "\n".join(schedule))
        
