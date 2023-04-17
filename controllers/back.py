from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from bot import BUTTONS, menu
from helper import get_user, update_user_steep


async def backs(message: types.Message):
    user = get_user(message)
    steep = user['steep']
    if steep == 'cars.menu' or steep == 'lessee.menu':
        update_user_steep(user['tg_id'], 'start')
        await message.answer('bu back', reply_markup=menu)

