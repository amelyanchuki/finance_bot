import sqlite3 as sq
from create_bot import bot



def new_sql():
    global base, cur
    base = sq.connect('financial_bot.db')
    cur = base.cursor()
    if base:
        print('Data base connected')
    base.execute('CREATE TABLE IF NOT EXISTS expenses(what_buy TEXT, price TEXT, date )')
    base.commit()


async def sql_add_expenses(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO expenses VALUES (?,?)', tuple(data.values()))
        base.commit()



async def sql_statisics_expenses(message):
    for ret in cur.execute('SELECT * FROM expenses').fetchall():
        await bot.send_message(message.from_user.id, f'{ret[0]}, {ret[1]}')
    