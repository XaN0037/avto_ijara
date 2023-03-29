from aiogram import Dispatcher, executor, types
from bot import BUTTONS,bot
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from helper import get_user, update_user_steep

async def handle_lessee(message: types.Message):
    user = get_user(message)
    steep = user['steep']
    if steep == 'lessee.menu':
        if message.text == BUTTONS['lesse_add']:
            await message.answer("Bu yerda qo'shish bajariladi")
        elif message.text == BUTTONS['lesse_get']:
            await message.answer("Bu ro'yxat chiqadi")
        elif message.text == BUTTONS['lesse_put']:
            await message.answer("Bu o'zgartiriladi")
        elif message.text == BUTTONS['lesse_delete']:
            await message.answer("Bu yerda o'chiriladi")
