from typing_extensions import _AnnotatedAlias
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from create_bot import dp
from aiogram.dispatcher.filters import Text
from data_base import sqlite_db
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from create_bot import bot

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

@dp.callback_query_handler(lambda x: x.data and x.data.startswith('del '))
async def delete_callback_run(callback_query: types.CallbackQuery):
    await sqlite_db.sql_delete_shoping_list(callback_query.data.replace('del ', ''))
    await callback_query.answer(text=f'{callback_query.data.replace("del ", "")} deleted.', show_alert=True)




async def delete_shoping_list(message: types.Message):
    read = await sqlite_db.sql_shop_list()
    for z in read:
        await bot.send_message(message.from_user.id, f'{z[0]}')
        await bot.send_message(message.from_user.id, text='^^^', reply_markup=InlineKeyboardMarkup().\
            add (InlineKeyboardButton(f'delete {z[0]}', callback_data=f'del {z[0]}')))



def register_hendler_shopping_list(dp: Dispatcher):
    dp.register_message_handler(start_shopping_list, commands='add_shopping_list', state= None)
    dp.register_message_handler(cancel_shoping_list, state="*", commands='cancel')
    dp.register_message_handler(cancel_shoping_list, Text(equals='/cancel', ignore_case=True), state="*")
    dp.register_message_handler(load_shoping_list, state=FSMShoping_list.what)
    dp.register_message_handler(watch_shoping_list, commands='shoping_list')
    # dp.callback_query_handler(delete_callback_run, lambda x: x.data and x.data.startswith('del '))
    # dp.callback_query_handler(delete_callback_run, Text(startswith='del '))
    dp.register_message_handler(delete_shoping_list, commands='delete_shoping_list')