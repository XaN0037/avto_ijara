import forloop as forloop
from aiogram import Dispatcher, executor, types
from bot import BUTTONS, bot
from helper import get_user, update_user_steep, dictfetchall, get_all_cars
import controllers.markups as nav

dp = Dispatcher(bot)


async def handle_cars(message: types.Message):
    user = get_user(message)
    steep = user['steep']
    if steep == 'cars.menu':
        cars = get_all_cars()
        if message.text == BUTTONS['get']:
            keyboard = types.InlineKeyboardMarkup(row_width=2)
            buttons = []
            for i in cars:
                buttons.append(f"{i['car_name']} No:{i['car_number']}")
            print(buttons,'bu yigiilgani','\n')
            for i in range(0,len(buttons)-1,2):
               print(i,'bu i',"\n")
               keyboard.add(
                        types.InlineKeyboardButton(text=f"{buttons[i]}", callback_data=f"{buttons[i]})"),
                        types.InlineKeyboardButton(text=f"{buttons[i+1]}", callback_data=f"{buttons[i+1]}"),
                            )

            keyboard.add(
                types.InlineKeyboardButton(text='back', callback_data='back'),
                types.InlineKeyboardButton(text='next', callback_data='next')

            )

            await message.answer(
                text=f"Bu Mashinalar ro'yxati {message.from_user.full_name}!",
                reply_markup=keyboard
            )

            # cars = get_all_cars()
            # print(cars, "\n\n\n")
            # car_name = []
            # car_number = []
            # car_color = []
            # for i in get_all_cars():
            #     car_name.append(i["car_name"])
            #     car_number.append(i["car_number"])
            #     car_color.append(i["car_color"])
            # await message.answer(f"1. {car_name[0]} raqami: {car_number[0]} rangi: {car_color[0]}\n"
            #                      f"2. {car_name[1]} raqami: {car_number[1]} rangi: {car_color[1]}", reply_markup=nav.mainMenu)

# @dp.callback_query_handler(text_contains="btn")
# async def pagination(call: types.callback_query):
#     await bot.delete_message(call.from_user.id, call.message_id)
#     print(call.data)
#     # await bot.send_message(message.from_user.id, "bu message", reply_markup=nav.mainMenu)


# @dp.callback_query_handler(text_contain="btnNext")
# async def pagination(message: types.Message):
#     await bot.delete_message(message.from_user.id, message.message_id)
#     await bot.send_message(message.from_user.id, "bu message", reply_markup=nav.mainMenu)
