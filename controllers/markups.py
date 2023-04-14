from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

mainMenu = InlineKeyboardMarkup(row_width=2)
btnBack = InlineKeyboardButton(text="Back", callback_data="btnBack")
btnNext = InlineKeyboardButton(text="Next", callback_data="btnNext")


mainMenu.insert(btnBack)
mainMenu.insert(btnNext)

