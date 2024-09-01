from datetime import datetime
from aiogram import Router, types, F
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from database import session_maker
from materials.models import Courses, Materials
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
# Состояния

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
    await message.answer("Введите ссылку")
    await state.set_state(AddCourses.link)

@admin_router.message(AddCourses.link, F.text)
async def add_link(message: types.Message, state: FSMContext, session: AsyncSession):
    await state.update_data(link=message.text)
    await message.answer(f"Добавлено", reply_markup=kb.admin_panel_menu)
    data = await state.get_data()

    obj = Courses(
        description=data["description"],
        link=data["link"]
    )

    session.add(obj)
    await session.commit()
    await message.answer(str(data))
    await state.clear()


# Добавление материалов
class AddMaterials(StatesGroup):
    description = State()
    link = State()
    
@admin_router.message(StateFilter(None), F.text == "Добавить материалы")
async def add_materials(message: types.Message, state: FSMContext):
    await message.answer(f"Введите описание", reply_markup=types.ReplyKeyboardRemove())
    await state.set_state(AddCourses.description)


@admin_router.message(AddCourses.description, F.text)
async def add_description(message: types.Message, state: FSMContext):
    await state.update_data(description=message.text)
    await message.answer("Введите ссылку")
    await state.set_state(AddCourses.link)

@admin_router.message(AddCourses.link, F.text)
async def add_link(message: types.Message, state: FSMContext, session: AsyncSession):
    await state.update_data(link=message.text)
    await message.answer(f"Добавлено", reply_markup=kb.admin_panel_menu)
    data = await state.get_data()

    obj = Materials(
        description=data["description"],
        link=data["link"]
    )

    session.add(obj)
    await session.commit()
    await message.answer(str(data))
    await state.clear()

@admin_router.message(F.text == "📋 Поправить расписание")
async def edit_python(message: types.Message):
    await message.answer("Выбирите команду", reply_markup=kb.admin_timesheet_menu)


# Добавление расписания
class AddTimesheet(StatesGroup):
    group = State()
    day = State()
    week = State()
    time = State()
    cabinet = State()
    subject = State()
    teacher = State()

    texts = {
        'AddTimesheet:group': 'Введите группу заново',
        'AddTimesheet:week': 'Введите тип недели заново',
        'AddTimesheet:day': 'Введите день недели заново',
        'AddTimesheet:time': 'Введите время заново',
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
        await message.answer(f"Введите корректный номер группы")
    else:
        await state.update_data(group=message.text)
        await message.answer("Введите тип недели")
        await state.set_state(AddTimesheet.week)


@admin_router.message(AddTimesheet.week, F.text)
async def add_day(message: types.Message, state: FSMContext):
    if message.text not in ["0", "1"]:
        await message.answer("Введите корректный тип недели 0 - чет, 1 - нечет")
    else:
        await state.update_data(week=message.text)
        await message.answer(f"Введите день недели")
        await state.set_state(AddTimesheet.day)


@admin_router.message(AddTimesheet.day, F.text)
async def add_time(message: types.Message, state: FSMContext):
    if (message.text not in ["1", "2", "3", "4", "5", "6"]):
        await message.answer("Введите корректный день недели")
    else:
        await state.update_data(day=message.text)
        await message.answer(f"Введите время")
        await state.set_state(AddTimesheet.time)


@admin_router.message(AddTimesheet.time, F.text)
async def add_cabinet(message: types.Message, state: FSMContext):
    await state.update_data(time=message.text)
    await message.answer(f"Введите кабинет")
    await state.set_state(AddTimesheet.cabinet)


@admin_router.message(AddTimesheet.cabinet, F.text)
async def add_subject(message: types.Message, state: FSMContext):
    if message.text.isnumeric() == False:
        await message.answer(f"Введите корректный номер кабинета")
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
    await message.answer(f"Добавлено", reply_markup=kb.admin_panel_menu)
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

class DeleteTimesheet(StatesGroup):
    id = State()


@admin_router.message(StateFilter(None), F.text == "Удалить расписание")
async def delete_timesheet_by_id(message: types.Message, state: FSMContext):

    await message.answer(f"Введите id расписания", reply_markup=types.ReplyKeyboardRemove())
    await state.set_state(DeleteTimesheet.id)


@admin_router.message(DeleteTimesheet.id, F.text)
async def delete_timesheet(message: types.Message, state: FSMContext, session: AsyncSession):
    timesheet_id = int(message.text)  
    await tm_request.delete_timesheet(session, timesheet_id)
    await message.answer(f"Расписание с id {timesheet_id} удалено")

    await state.clear()


@admin_router.message(F.text == "Вся информация")
async def edit_python(message: types.Message, session: AsyncSession):
    timesheets = await tm_request.get_all_info(session)

    weekly_schedule = {}

    for timesheet in timesheets:
        if timesheet.day not in weekly_schedule:
            weekly_schedule[timesheet.day] = []
        weekly_schedule[timesheet.day].append(f"{timesheet.id}, {timesheet.group}, {timesheet.week}, {timesheet.day}, {timesheet.time}, {timesheet.cabinet}, {timesheet.subject}, {timesheet.teacher}")
    
    for day, schedule in weekly_schedule.items():
        await message.answer(f"--- {day} ---\n" + "\n".join(schedule))
    
    await message.answer("Все Расписание")