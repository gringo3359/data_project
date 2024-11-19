from telegram import Bot
from sqlalchemy import text
import datetime as dt
import pandas as pd
import db_connection as dbcon
import asyncio

with dbcon.engine.connect() as connection:
    query = text(f'SELECT * FROM the_oldest_people_by_countries')
    result = connection.execute(query)
    df = pd.DataFrame(result.fetchall(), columns=result.keys())


csv_file = f'{dt.datetime.now()}.csv'
df.to_csv(csv_file, index=False)

file_path = '/Users/onetwo/Downloads/tg.txt'

with open(file_path, 'r') as file:
    tg = file.readline().split()

bot = Bot(token=tg[0])

with open(csv_file, 'rb') as file:
    asyncio.run(bot.send_document(chat_id=tg[1], document=file))

