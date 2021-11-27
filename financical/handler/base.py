from aiogram import types
from aiogram.dispatcher.dispatcher import Dispatcher
from create_bot import dp
from keybords import kb_client



async def command_start(message: types.Message):
    await message.reply('Good day. This bot is used to record all expenses and incomes for the purpose of collecting statistics and building graphs.The bot\'s functionality will increase over time. If you have any suggestions for improving it, write them to the bot by typing "/pls_update" beforehand. Thanks for using ^ _ ^.',
    reply_markup=kb_client)


async def command_help(message: types.Message):
    await message.reply('Soon ^_^')

def register_hendler_base(dp: Dispatcher):
    dp.register_message_handler(command_start, commands='start')
    dp.register_message_handler(command_help, commands='help')    