import os
from PIL import Image
from pytesseract import pytesseract

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from .keyboard import T_buttons
from app.utils.config_reader import load_config




config = load_config("config/bot.ini")


class TextFinderStates(StatesGroup):
    waitingForPhoto = State()


async def start_photo_handler(message: types.Message, state: FSMContext) -> None:
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
    keyboard.add(*T_buttons)

    await message.answer(f"Отправь мне фото, а я скажу что за текст на нем😎", reply_markup = keyboard)
    await state.set_state(TextFinderStates.waitingForPhoto.state)


async def photo_handler(message: types.Message) -> None:
    pytesseract.tesseract_cmd = config.tg_bot.path_to_tesseract

    file_id = message.photo[-1].file_id
    destination_file = config.tg_bot.path_for_photo + f"\{file_id}.png"
    
    await message.photo[-1].download(destination_file = destination_file)

    text = pytesseract.image_to_string(Image.open(destination_file), lang='rus')
    if text : await message.answer(text[:-1])
    else: await message.answer("У меня не получилось ничего распознать🥺🤒")


async def stop_photo_handler(message: types.Message, state: FSMContext) -> None:
    await message.answer("Как скажешь🥱", reply_markup = types.ReplyKeyboardRemove())

    for file in os.scandir(config.tg_bot.path_for_photo):
        os.remove(file.path)

    await state.finish()
