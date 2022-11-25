import asyncio

from aiogram import types
from aiogram.dispatcher import FSMContext

from config.commands import my_commands
from ..utils.actions import get_us_name, send_launch_info, send_action, send_service_info


def get_commands_list()  -> str:
    commands_list = "\n"
    for x in my_commands:
        commands_list += str(x.command + " – " + x.description + "\n")
    return commands_list

async def cmd_start(message: types.Message, state: FSMContext) -> None:
    await state.finish()

    await send_launch_info(message)

    await message.answer(f"Ого😳 Кто это к нам пожаловал😑", reply_markup = types.ReplyKeyboardRemove())
    await send_action(message, 1, types.ChatActions.CHOOSE_STICKER)
    await message.answer_sticker("CAACAgIAAxkBAAEE-eVipcF2qbxR3pK8PaZ6PR3oWDWx0wACqQ0AApI2owtpmctsM8-quCQE")
    await send_action(message, 1)
    await message.answer(f"Ну-ка руки вверх!! И подожди секундочку, я подумаю🥱")
    await asyncio.sleep(5)
    await message.answer(f"А ой, так это ведь {get_us_name(message)} собственой персоны")
    await send_action(message, 1, types.ChatActions.CHOOSE_STICKER)
    await message.answer_sticker("CAACAgIAAxkBAAEE-e5ipcT1ppvPyRlDK1mUq2s_SYMFIwACpg0AApI2owt0vnIsURd_2iQE")
    await send_action(message, 3)
    await message.answer(f"Привет, привет!! Я знаю парочку команд:{get_commands_list()}")
    await send_action(message, 1)
    await message.answer(f"Что делать будем?👀")
    
async def cmd_help(message: types.Message) -> None:
    await message.answer(f"Так... Кажется {get_us_name(message)} нужна помощь?)")
    await message.answer(f"Вот те команды что я знаю: {get_commands_list()}")

async def cmd_exit(message: types.Message, state: FSMContext) -> None:
    await state.finish()

    msg = await message.answer(f"Состояние сброшено!")
    await asyncio.sleep(1)

    await msg.edit_text(f"Привет, привет!! Я знаю парочку команд:{get_commands_list()}")
    await send_action(message, 1)
    await message.answer(f"Что делать будем?👀", reply_markup = types.ReplyKeyboardRemove())

async def unindentified_messages(message: types.Message) -> None:
    await send_service_info(message)
    await message.answer(f"Погоди, я еще не такой умный✋😔")    