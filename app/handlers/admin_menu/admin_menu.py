from random import choice

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from app.utils.config_reader import load_config




config = load_config("config/bot.ini")

answers = ["Даже не пытайся🥱🙃",
            "Кыш😤😠",
            "Ты уверен в своих силах?)",
            "Скукотища😩😔",
            "Ты почти угадал🙄🙄"
]


class AdminMenuStates(StatesGroup):
    waitingForAdminPass = State()


async def admin_menu(message: types.Message, state: FSMContext) -> None:
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
    keyboard.add("Сдаться")

    if message.chat.id == config.tg_bot.admin_id:
        await message.answer("Привет, s19!")
        return

    await message.answer(f"А ты точно s19? Ну-ка введи пароль:", reply_markup = keyboard)
    await state.set_state(AdminMenuStates.waitingForAdminPass.state)


async def pass_check(message: types.Message, state: FSMContext) -> None:
    if message.text != config.tg_bot.admin_pass:
        await message.answer(choice(answers))
        return

    await message.answer("Хоть ты и угадал пароль, я тебе ничего не скажу!!", reply_markup = types.ReplyKeyboardRemove())
    await state.finish()


async def exit_from_admin_menu(message: types.Message, state: FSMContext) -> None:
    await message.answer("Давно пора было сдаться🥱", reply_markup = types.ReplyKeyboardRemove())
    await state.finish()