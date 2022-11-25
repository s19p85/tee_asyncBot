import configparser
from dataclasses import dataclass




@dataclass
class TgBot:
    token: str
    admin_id: int
    service_chat : int
    admin_pass : str
    path_for_photo : str
    path_to_tesseract : str


@dataclass
class Config:
    tg_bot: TgBot


def load_config(path: str):
    config = configparser.ConfigParser()
    config.read(path)

    tg_bot = config["tg_bot"]

    return Config(
        tg_bot=TgBot(
            token=tg_bot["token"],
            admin_id=int(tg_bot["admin_id"]),
            service_chat=int(tg_bot["service_chat"]),
            admin_pass=tg_bot["admin_pass"],
            path_for_photo=tg_bot["path_for_photo"],
            path_to_tesseract=tg_bot["path_to_tesseract"]
        )
    )
