from aiogram import types
from database.dao.holder import DAO
from keyboards.reply import start_button


async def start(message: types.Message, dao: DAO):
    await message.answer("HI!", reply_markup=await start_button())
    await dao.user.create(message.chat.id, message.chat.full_name, message.chat.username)
