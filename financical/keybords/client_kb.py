from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('/expenses')
b2 = KeyboardButton('/income')
b3 = KeyboardButton('/statistics')
b4 = KeyboardButton('/shopping_list')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)


kb_client.add(b1).row(b2, b3, b4)

