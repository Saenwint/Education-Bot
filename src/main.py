import asyncio
import logging
from config import config
from handlers.handler import dp
from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode


logging.basicConfig(level=logging.INFO)

bot = Bot(
    token=config.bot_token.get_secret_value(),
    default=DefaultBotProperties(
    parse_mode=ParseMode.MARKDOWN_V2
    )
)



async def main():
    await dp.start_polling(bot)
    
asyncio.run(main())