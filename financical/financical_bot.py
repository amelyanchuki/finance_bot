from aiogram.utils import executor
from aiohttp import client
from create_bot import dp
async def bot_up(_):
    print('Bot is online')

from handler import base, expenses, pls_update, shopping_list, statistics, income, sorry

base.register_hendler_base(dp)
income.register_hendler_income(dp)
statistics.register_hendler_statistics(dp)
shopping_list.register_hendler_shopping_list(dp)
pls_update.register_hendler_pls_update(dp)
expenses.register_hendler_expenser(dp)
sorry.register_hendler_sorry(dp)



executor.start_polling(dp, skip_updates=True, on_startup=bot_up)