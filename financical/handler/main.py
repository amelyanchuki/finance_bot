from aiogram import types, Dispatcher
from create_bot import dp

async def command_expenses(message: types.Message):#расходы
    await message.reply('Soon ^_^')

async def command_income(message: types.Message):#доходы
    await message.reply('Soon ^_^')

async def command_statistics(message: types.Message):#статистика
    await message.reply('Soon ^_^')

async def command_shopping_list(message: types.Message):#список покупок
    await message.reply('Soon ^_^')


async def command_pls_update(message: types.Message):#pls update
    await message.reply('w8 ^_^')


async def echo_send(message : types.Message):
    await message.reply(message.text)


def register_hendler_main(dp: Dispatcher):
    dp.register_message_handler(command_expenses, commands='expenses')
    dp.register_message_handler(command_income, commands='income')
    dp.register_message_handler(command_statistics, commands='statistics')
    dp.register_message_handler(command_shopping_list, commands='shopping_list')
    dp.register_message_handler(command_pls_update, commands='pls_update')
    dp.register_message_handler(echo_send)