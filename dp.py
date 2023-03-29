from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from bot import bot, BUTTONS
from controllers.cars import handle_cars
from controllers.lessee import handle_lessee
from helper import get_user, update_user_steep

dp = Dispatcher(bot)


@dp.message_handler(commands=['cars'])
async def cars(message: types.Message):
    await handle_cars(message)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
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


@dp.message_handler()
async def echo(message: types.Message):
    user = get_user(message)
    steep = user['steep'].split('.')[0]
    if steep == 'start':
        if message.text == BUTTONS['cars']:
            update_user_steep(user['tg_id'], 'cars.menu')
            menu = ReplyKeyboardMarkup(
                keyboard=[
                    [
                        KeyboardButton(text=BUTTONS['get']),
                        KeyboardButton(text=BUTTONS['add'])
                    ],
                    [
                        KeyboardButton(text=BUTTONS["put"]),
                        KeyboardButton(text=BUTTONS['delete'])
                    ],
                    [
                        KeyboardButton(text=BUTTONS["back"])
                    ]
                ],
                resize_keyboard=True)
            await message.answer('bu start', reply_markup=menu)

    elif steep == 'cars':
        await handle_cars(message)

    if message.text == BUTTONS['lessee']:
        update_user_steep(user['tg_id'], 'lessee.menu')
        menu = ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text=BUTTONS['lesse_get']),
                    KeyboardButton(text=BUTTONS['lesse_add'])
                ],
                [
                    KeyboardButton(text=BUTTONS["lesse_put"]),
                    KeyboardButton(text=BUTTONS['lesse_delete'])
                ],
                [
                    KeyboardButton(text=BUTTONS["back"]),
                ]
            ],

            resize_keyboard=True)
        await message.answer('bu ijarachilar', reply_markup=menu)
    if steep == "cars.menu":
        if message.text == BUTTONS['back']:
            print('orqagaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
    elif steep == 'lessee':
        await handle_lessee(message)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
