from typing_extensions import _AnnotatedAlias
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from create_bot import dp
from aiogram.dispatcher.filters import Text
from data_base import sqlite_db

class FSMShoping_list(StatesGroup):
    what = State()


async def start_shopping_list(message: types.Message):#список покупок
    await FSMShoping_list.what.set()
    await message.reply("What do you want to buy?")




async def cancel_shoping_list(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('Ok')



async def load_shoping_list(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['what'] = message.text
    
    await sqlite_db.sql_add_shoping_list(state)
    await state.finish() 


async def watch_shoping_list(message: types.Message):
    await sqlite_db.sql_shoping_list(message)







def register_hendler_shopping_list(dp: Dispatcher):
    dp.register_message_handler(start_shopping_list, commands='add_shopping_list', state= None)
    dp.register_message_handler(cancel_shoping_list, state="*", commands='cancel')
    dp.register_message_handler(cancel_shoping_list, Text(equals='/cancel', ignore_case=True), state="*")
    dp.register_message_handler(load_shoping_list, state=FSMShoping_list.what)
    dp.register_message_handler(watch_shoping_list, commands='shoping_list')