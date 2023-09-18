import asyncio
from typing import Optional

from aiogram import Dispatcher, Bot
from aiogram.enums import ParseMode
from loguru import logger

from config import TgBotConfig
from tg_bot.handlers import registry_users_handler

_dispatcher: Dispatcher = Optional[None]


def registry_handlers() -> None:
    logger.info('tg_bot registry handlers')
    registry_users_handler(dp=_dispatcher)


def on_startup(bot: Bot):
    pass


async def main(tg_bot_config: TgBotConfig):
    global _dispatcher

    _dispatcher = Dispatcher()
    _dispatcher.startup.register(on_startup)
    bot: Bot = Bot(token=tg_bot_config.token, parse_mode=ParseMode.HTML)

    registry_handlers()

    await _dispatcher.start_polling(bot)


def start(tg_bot_config: TgBotConfig) -> None:
    asyncio.run(main(tg_bot_config=tg_bot_config))
