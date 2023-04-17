from aiogram import executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from bot import bot, BUTTONS, dp, menu
from controllers.back import backs
from controllers.cars import handle_cars
from controllers.lessee import handle_lessee
from helper import get_user, update_user_steep, update_inline_page, get_all_cars
from controllers.markups import inline_btn


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    user = get_user(message)
    update_user_steep(user['tg_id'], 'start')
    update_inline_page(user['tg_id'], 1)
    await message.answer('bu start', reply_markup=menu)


@dp.callback_query_handler(text_contains="btn")
async def pagination(call: types.callback_query):
    await bot.delete_message(call.from_user.id, call.message.message_id)
    user = get_user(call)
    page = int(user.get('inline_page'))
    if call.data == "btnNext":
        if page >= 2:
            page = 1
        else:
            page += 1
        await bot.send_message(call.from_user.id, f"Mashinalar soni:  {len(get_all_cars())}  ta", reply_markup=inline_btn(page))

    elif call.data == "btnBack":
        if page == 1:
            await bot.send_message(call.from_user.id, "bundan oldinda page yoq", reply_markup=inline_btn(page))
        else:
            page -= 1
            await bot.send_message(call.from_user.id, f"Mashinalar soni:  {len(get_all_cars())}  ta", reply_markup=inline_btn(page))

    update_inline_page(user['tg_id'], page)


@dp.callback_query_handler(text_contains="CaR")
async def pagination(call: types.callback_query):
    # await bot.delete_message(call.from_user.id, call.message.message_id)
    print(call.data)


@dp.message_handler()
async def echo(message: types.Message):
    user = get_user(message)
    steep = user['steep'].split('.')[0]
    if message.text == BUTTONS['back']:
        await backs(message)

    if steep == 'start':
        if message.text == BUTTONS['cars']:
            update_user_steep(user['tg_id'], 'cars.menu')
            menu = ReplyKeyboardMarkup(
                keyboard=[
                    [KeyboardButton(text=BUTTONS['get'])],
                    [KeyboardButton(text=BUTTONS["back"])]
                ], resize_keyboard=True)
            await message.answer('bu cars', reply_markup=menu)

    elif steep == 'cars':
        await handle_cars(user, message)

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
    elif steep == 'lessee':
        await handle_lessee(message)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)