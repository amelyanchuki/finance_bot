from aiogram import types, Dispatcher
from create_bot import dp

    


async def sorry(message : types.Message):
    await message.reply("I dont understend you, sorry T_T")


def register_hendler_sorry(dp: Dispatcher):
    dp.register_message_handler(sorry)
