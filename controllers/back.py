from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from bot import BUTTONS
# from dp import start
from helper import get_user, update_user_steep


async def backs(message: types.Message):
    user = get_user(message)
    steep = user['steep']
    if steep == 'cars.menu' or steep == 'lessee.menu':
        user = get_user(message)
        try:
            steep = user['steep'].split('.')[0]
        except:
            steep = ''
        update_user_steep(user['tg_id'], 'start')
        menu = ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text=BUTTONS['cars'])
                ],
                [
                    KeyboardButton(text=BUTTONS['lessee'])
                ]
            ],
            resize_keyboard=True)
        await message.answer('bu start', reply_markup=menu)
