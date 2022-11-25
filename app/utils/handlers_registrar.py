from aiogram import Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.types.message import ContentType

from ..handlers.common import cmd_start, cmd_help, cmd_exit, unindentified_messages
from ..handlers.questions.questions_handler import start_questions, questions, stop_questions, QuestionsStates
from ..handlers.admin_menu.admin_menu import admin_menu, pass_check, exit_from_admin_menu, AdminMenuStates
from ..handlers.text_finder.text_finder import start_photo_handler, photo_handler, stop_photo_handler, TextFinderStates




def handlers_registrar(dp: Dispatcher) -> None:
    #common
    dp.register_message_handler(cmd_start, commands="start", state="*")
    dp.register_message_handler(cmd_help, commands="help", state="*")
    dp.register_message_handler(cmd_exit, commands="exit", state="*")


    #admin_menu
    dp.register_message_handler(admin_menu, commands="s19", state="*")
    dp.register_message_handler(exit_from_admin_menu, Text(equals="сдаться", ignore_case=True), state=AdminMenuStates.waitingForAdminPass)
    dp.register_message_handler(pass_check, state=AdminMenuStates.waitingForAdminPass)


    #questions
    dp.register_message_handler(start_questions, commands="questions", state="*")
    dp.register_message_handler(stop_questions, Text(equals="не хочу спрашивать🥱", ignore_case=True), state=QuestionsStates.waitingForQuestion)
    dp.register_message_handler(questions, state=QuestionsStates.waitingForQuestion)


    #text_finder
    dp.register_message_handler(start_photo_handler, commands="find_text", state="*")
    dp.register_message_handler(stop_photo_handler, Text(equals="все! у меня картинки кончились🥱", ignore_case=True), state=TextFinderStates.waitingForPhoto)
    dp.register_message_handler(photo_handler, content_types = ContentType.PHOTO, state=TextFinderStates.waitingForPhoto)


    dp.register_message_handler(unindentified_messages, content_types = ContentType.ANY)