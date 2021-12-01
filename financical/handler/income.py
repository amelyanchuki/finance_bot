from aiogram import types, Dispatcher
from create_bot import dp
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text

class FSMIncome(StatesGroup):
    income = State()
    how = State()



async def start_income(message: types.Message):
    await FSMIncome.income.set()
    await message.reply('Where did you make your money?')

async def cancel_income(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('Ok')


async def load_income(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['income'] = message.text
    await FSMIncome.next()
    await message.reply('How much did you earn?')



async def load_how(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['how'] = float(message.text)

    async with state.proxy() as data:
        await message.reply(str(data))
    await state.finish()

# async def command_income(message: types.Message):#доходы
#     await message.reply('Soon ^_^')




def register_hendler_income(dp: Dispatcher):
    dp.register_message_handler(start_income, commands='income', state=None)
    dp.register_message_handler(cancel_income, state="*", commands='cancel')
    dp.register_message_handler(cancel_income, Text(equals='cancel', ignore_case=True), state="*")
    dp.register_message_handler(load_income, state=FSMIncome.income)
    dp.register_message_handler(load_how, state=FSMIncome.how)
    # dp.register_message_handler(command_income, commands='income')