from telegram import Bot
from sqlalchemy import text
import os
from dotenv import load_dotenv
import datetime as dt
import pandas as pd
import db_connection as dbcon
import asyncio

load_dotenv()

telegram_bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
chat_id = os.getenv('CHAT_ID')

with dbcon.engine.connect() as connection:
    query = text(f'SELECT * FROM the_oldest_people_by_countries')
    result = connection.execute(query)
    df = pd.DataFrame(result.fetchall(), columns=result.keys())

csv_file = f'{dt.datetime.now()}.csv'
df.to_csv(csv_file, index=False)

bot = Bot(token=telegram_bot_token)

with open(csv_file, 'rb') as file:
    asyncio.run(bot.send_document(chat_id=chat_id, document=file))

