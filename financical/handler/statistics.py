from aiogram import types, Dispatcher
from create_bot import dp
from data_base import sqlite_db

async def command_statistics(message: types.Message):
    await sqlite_db.sql_statisics_expenses(message)
    await sqlite_db.sql_statistics_income(message)



def register_hendler_statistics(dp: Dispatcher):
    dp.register_message_handler(command_statistics, commands='statistics')