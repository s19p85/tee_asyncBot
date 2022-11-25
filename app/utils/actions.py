import asyncio
from datetime import datetime

from aiogram import types
from aiogram.types import ChatActions

from app.utils.config_reader import load_config




config = load_config("config/bot.ini")


def get_us_name(message : types.Message) -> str:
     usName = str(message.from_user.first_name)
     if str(message.from_user.last_name).lower() != "none": usName += (" " + str(message.from_user.last_name))
     return usName


async def send_launch_info(message : types.Message) -> None:
    if message.chat.id != config.tg_bot.admin_id:
        launchInfo = f"<b><u>Event!</u></b>\n\n<i>The TEEBOT was launched by the user {get_us_name(message)} (@{message.from_user.username}) [ID: <code>{message.from_user.id}</code>]\n{datetime.now().strftime('%Y-%m-%d at %H:%M:%S')}(UTC+4)\n\n#NewUser</i>"
        await message.bot.send_message(config.tg_bot.service_chat, launchInfo, parse_mode='html')


async def send_action(message : types.Message, timing : int, action = ChatActions.TYPING) -> None:
    await message.bot.send_chat_action(message.chat.id, action = action)
    await asyncio.sleep(timing)


async def send_service_info(message : types.Message) -> None:
    if message.chat.id != config.tg_bot.admin_id:
        serviceData = f"<b><u>Date & Time:</u></b>\n<i>{datetime.now().strftime('%Y-%m-%d   %H:%M:%S')}(UTC+4)</i>\n\n<b><u>From:</u></b> <i>{message.from_user.first_name}</i> (@{message.from_user.username})\n\n<b><u>Text:</u></b>\n\"{message.text}\""
        await message.bot.send_message(config.tg_bot.service_chat, serviceData, parse_mode='html')
        if str(message.text).lower() == "none": await message.bot.forward_message(config.tg_bot.service_chat, message.chat.id, message.message_id)
