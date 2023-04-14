import logging
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5739426670:AAFcmdIa5bN6SvMg7oqYeTbU7r0G7grw6F0'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

BUTTONS = {
    "cars": "🚘 Mashinalar",
    "add": "Qo'shish",
    "get": "Ro'yxat",
    "put": "O'zgartirish",
    "delete": "O'chirish",

    "lessee": "👨‍✈️Ijarachilar",
    "lesse_add": "Qo'shish",
    "lesse_get": "Ro'yxat",
    "lesse_put": "O'zgartirish",
    "lesse_delete": "O'chirish",

    "back": "Back",
    "next": "Next"
}

from helper import *
from controllers.cars import handle_cars

# import pprint

# @dp.message_handler()
# async def echo(message: types.Message):
#     user = get_user(message)
#     message['bot_user'] = user
#     pp = pprint.PrettyPrinter(indent=4)
#     print("------------------------------------------")
#     pp.pprint(dict(message))
#     print("------------------------------------------")
#
#     await message.answer(message.text)
