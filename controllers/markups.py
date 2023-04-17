from aiogram import types
from helper import get_all_cars

# mainMenu = InlineKeyboardMarkup(row_width=2)
# btnBack = InlineKeyboardButton(text="Back", callback_data="btnBack")
# btnNext = InlineKeyboardButton(text="Next", callback_data="btnNext")
#
# mainMenu.insert(btnBack)
# mainMenu.insert(btnNext)


def inline_btn(page):
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    cars = get_all_cars()
    limit = page * 8
    offset = (page - 1) * 8
    car = []
    j = 0
    for n in cars:
        j += 1
        car.append(f"{j}. {n['car_name']}  {n['car_number']}")
    print(car, '\n')
    for i in range(offset, limit, 2):
        try:
            keyboard.add(
                types.InlineKeyboardButton(text=f"{car[i]}", callback_data=f"CaR{i+1}"),
                types.InlineKeyboardButton(text=f"{car[i + 1]}", callback_data=f"CaR{i + 2}")
            )
        except:
            try:
                keyboard.add(types.InlineKeyboardButton(text=f"{car[i]}", callback_data=f"CaR{i+1}"))
            except:
                break

    keyboard.add(
        types.InlineKeyboardButton(text="Back", callback_data="btnBack"),
        types.InlineKeyboardButton(text="Next", callback_data="btnNext")
    )

    return keyboard
