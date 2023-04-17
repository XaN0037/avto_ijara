from aiogram import types
from bot import BUTTONS, bot
from helper import get_all_cars
from controllers.markups import inline_btn


async def handle_cars(user, message: types.Message):
    steep = user['steep']
    if steep == 'cars.menu':
        if message.text == BUTTONS['get']:
            page = int(user.get('inline_page'))
            await bot.send_message(message.from_user.id, text=f"Mashinalar soni:  {len(get_all_cars())}  ta",
                                   reply_markup=inline_btn(page))

