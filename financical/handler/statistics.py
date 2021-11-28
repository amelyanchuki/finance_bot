from aiogram import types, Dispatcher
from create_bot import dp


async def command_statistics(message: types.Message):#статистика
    await message.reply('Soon ^_^')







def register_hendler_statistics(dp: Dispatcher):
    dp.register_message_handler(command_statistics, commands='statistics')