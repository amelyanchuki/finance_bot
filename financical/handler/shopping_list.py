from aiogram import types, Dispatcher
from create_bot import dp


async def command_shopping_list(message: types.Message):#список покупок
    await message.reply('Soon ^_^')







def register_hendler_shopping_list(dp: Dispatcher):
    dp.register_message_handler(command_shopping_list, commands='shopping_list')