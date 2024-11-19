from telegram import Bot
from sqlalchemy import text
import datetime as dt
import pandas as pd
import db_connection as dbcon
import asyncio

#591237445
with dbcon.engine.connect() as connection:
    query = text(f'SELECT * FROM the_oldest_people_by_countries')
    result = connection.execute(query)
    df = pd.DataFrame(result.fetchall(), columns=result.keys())


csv_file = f'{dt.datetime.now()}.csv'
df.to_csv(csv_file, index=False)

telegram_token = '7668577240:AAFHnCVhZw-K5iWU-B7SLhqjmFXnjz3muTg'
chat_id = '591237445'

bot = Bot(token=telegram_token)

with open(csv_file, 'rb') as file:
    asyncio.run(bot.send_document(chat_id=chat_id, document=file))

