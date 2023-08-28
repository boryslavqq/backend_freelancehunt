from aiogram import Dispatcher
from aiogram.dispatcher.filters import CommandStart

from handlers.menu import start


def setup(dp: Dispatcher):
    dp.register_message_handler(start, CommandStart())
