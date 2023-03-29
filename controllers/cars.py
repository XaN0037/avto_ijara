from aiogram import Dispatcher, executor, types
from bot import BUTTONS,bot
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from helper import get_user, update_user_steep

async def handle_cars(message: types.Message):
    user = get_user(message)
    steep = user['steep']
    if steep == 'cars.menu':
        if message.text == BUTTONS['add']:
            await message.answer("Bu yerda qo'shish bajariladi")
        elif message.text == BUTTONS['get']:
            await message.answer("Bu ro'yxat chiqadi")
        elif message.text == BUTTONS['put']:
            await message.answer("Bu o'zgartiriladi")
        elif message.text == BUTTONS['delete']:
            await message.answer("Bu yerda o'chiriladi")

