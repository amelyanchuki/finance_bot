from aiogram import types, Dispatcher
from create_bot import dp


async def command_pls_update(message: types.Message):#pls update
    await message.reply('w8 ^_^')



def register_hendler_pls_update(dp: Dispatcher):
    dp.register_message_handler(command_pls_update, commands='pls_update')