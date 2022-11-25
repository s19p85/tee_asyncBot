from random import choice

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from .answers import Q_answers
from .keyboard import Q_buttons




class QuestionsStates(StatesGroup):
    waitingForQuestion = State()


async def start_questions(message: types.Message, state: FSMContext) -> None:
    keyboard = types.ReplyKeyboardMarkup(row_width = 2, resize_keyboard = True)
    keyboard.add(*Q_buttons)

    await message.answer(f"Задай вопрос нажав на кнопочку🥱", reply_markup = keyboard)
    await state.set_state(QuestionsStates.waitingForQuestion.state)


async def questions(message: types.Message) -> None:
    question = message.text.lower()

    match question: 
        case "о чем тебя спросить?": 
            await message.answer(f"Спроси меня \"{choice(Q_answers[0])}\"")
        case "что ты умеешь?": 
            await message.answer(choice(Q_answers[1]))
        case "как дела?": 
            await message.answer(choice(Q_answers[2]))
        case "какая погода сегодня?": 
            await message.answer(choice(Q_answers[3]))
        case "поиграем?": 
            await message.answer(choice(Q_answers[4]))
        case _: 
            await message.answer_sticker("CAACAgIAAxkBAAEGEYVjRwR0jY4Nbq_hoUM7GH1ww-Y8rQACrA0AApI2owvPK_LUm0j_5SoE")


async def stop_questions(message: types.Message, state: FSMContext) -> None:
    await message.answer("Как скажешь🥱", reply_markup = types.ReplyKeyboardRemove())
    await state.finish()
