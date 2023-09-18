from aiogram import Dispatcher, Router
from aiogram.filters import Command
from aiogram.types import Message

user_router = Router()


@user_router.message(Command("start"))
async def handler_start(message: Message):
    await message.reply(f'Eeeee, boy\n{message.from_user}')


def registry_users_handler(dp: Dispatcher):
    dp.include_router(user_router)
    # user_router.message(handler_start, Command("start"))
