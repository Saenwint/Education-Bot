import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.fsm.strategy import FSMStrategy
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

from config import config
from middlewares.db import DataBaseSession
from database import create_db, drop_db, session_maker
from handlers.user_handlers import user_router
from handlers.admin_handlers import admin_router

logging.basicConfig(level=logging.INFO)

dp = Dispatcher(fsm_strategy = FSMStrategy.USER_IN_CHAT,)

dp.include_router(admin_router)
dp.include_router(user_router)

bot = Bot(
    token=config.bot_token.get_secret_value(),
    default=DefaultBotProperties(
    #parse_mode=ParseMode.MARKDOWN_V2
    parse_mode=ParseMode.HTML
    )
)

async def on_startup(bot):
    print('bot start')
    await create_db()


async def on_shutdown(bot):
    print('shutdown bot')
    await drop_db()


@dp.message(F.text == "id")
async def get_id(message: types.Message):
    await message.answer(f"Ваш id: {message.from_user.id}")


async def main():
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)

    dp.update.middleware(DataBaseSession(session_pool=session_maker))

    await bot.delete_webhook(drop_pending_updates=True)
    
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    
asyncio.run(main())