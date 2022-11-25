import os
import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from app.utils.config_reader import load_config
from config.commands import my_commands
from app.utils.handlers_registrar import handlers_registrar




logger = logging.getLogger(__name__)


async def main():
    os.system("type Header.txt")

    logging.basicConfig(
        level=logging.INFO,
        format="   %(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )
    logger.info("Starting bot")

    config = load_config("config/bot.ini")

    bot = Bot(token=config.tg_bot.token)
    dp = Dispatcher(bot, storage=MemoryStorage())

    handlers_registrar(dp)

    await bot.set_my_commands(my_commands)

    await dp.skip_updates()
    await dp.start_polling()


if __name__ == '__main__':
    asyncio.run(main())

