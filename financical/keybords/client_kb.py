from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('/expenses')
b2 = KeyboardButton('/income')
b3 = KeyboardButton('/statistics')
b4 = KeyboardButton('/add_shopping_list')
b5 = KeyboardButton('/shoping_list')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)


kb_client.row(b1, b2, b3).row(b4, b5)

