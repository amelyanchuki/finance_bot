import sqlite3 as sq

from aiogram.types import message
from create_bot import bot



def new_sql():
    global base, cur
    base = sq.connect('financial_bot.db')
    cur = base.cursor()
    if base:
        print('Data base connected')
    base.execute('CREATE TABLE IF NOT EXISTS expenses(what_buy TEXT, price TEXT)')
    base.commit()
    base.execute('CREATE TABLE IF NOT EXISTS income(how TEXT, income TEXT)')
    base.commit
    base.execute('CREATE TABLE IF NOT EXISTS shoping_list(what_u_want TEXT)')


async def sql_add_expenses(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO expenses VALUES (?,?)', tuple(data.values()))
        base.commit()



async def sql_statisics_expenses(message):
    for ret in cur.execute('SELECT * FROM expenses').fetchall():
        await bot.send_message(message.from_user.id, f'{ret[0]}, {ret[1]}')

async def sql_add_income(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO income VALUES (?,?)', tuple(data.values()))
        base.commit()

async def sql_statistics_income(message):
    for x in cur.execute('SELECT * From income').fetchall():
        await bot.send_message(message.from_user.id, f'{x[0]},{x[1]}' )


async def sql_add_shoping_list(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO shoping_list VALUES(?)', tuple(data.values()))
        base.commit()

async def sql_shoping_list(message):
    for z in cur.execute('SELECT * FROM shoping_list').fetchall():
        await bot.send_message(message.from_user.id, f'{z[0]}')

async def sql_shop_list():
    return cur.execute('SELECT * FROM shoping_list').fetchall()

async def sql_delete_shoping_list(data):
    cur.execute('DELETE FROM shoping_list WHERE what_u_want == ?', (data,))
    base.commit()
    
