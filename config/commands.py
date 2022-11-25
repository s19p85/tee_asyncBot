from aiogram.types import BotCommand




my_commands = [
        BotCommand(command="/start", description="👾launch a bot"),
        BotCommand(command="/questions", description="🥱experts, attention to the question..."),
        BotCommand(command="/find_text", description="😎i can find the text on the photo"),
        BotCommand(command="/help", description="🤔u wanna be helped?"),
        BotCommand(command="/exit", description="🤒emergency reset of state"),
        BotCommand(command="/s19", description="❌staff only"),
]