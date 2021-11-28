from aiogram import types, Dispatcher
from create_bot import dp
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text


class FSMExpenses(StatesGroup):
    what_buy = State()
    what_price = State()



async def start_expenses(message: types.Message):
    await FSMExpenses.what_buy.set()
    await message.reply('What did you buy?')



async def load_what_buy(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['what_buy'] = message.text
    await FSMExpenses.next()
    await message.reply('How much did you buy?')



async def load_what_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['what_price'] = float(message.text)

    async with state.proxy() as data:
        await message.reply(str(data))
    await state.finish()

async def cancel_expenser(message: types.Message, state: FSMContext):
    current_state = await state.get()
    if current_state is None:
        return
    await state.finish()
    await message.reply('Ok')




def register_hendler_expenser(dp: Dispatcher):
    dp.register_message_handler(start_expenses, commands='expenses', state=None)
    dp.register_message_handler(load_what_buy, state=FSMExpenses.what_buy)
    dp.register_message_handler(load_what_price, state=FSMExpenses.what_price)
    dp.register_message_handler(cancel_expenser, state="*", commands='cancel')
    dp.register_message_handler(cancel_expenser, Text(equals='cancel', ignore_case=True), state="*")