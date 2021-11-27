from aiogram.utils import executor
from aiohttp import client
from create_bot import dp
async def bot_up(_):
    print('Bot is online')

from handler import base, main

base.register_hendler_base(dp)
main.register_hendler_main(dp) 

executor.start_polling(dp, skip_updates=True, on_startup=bot_up)