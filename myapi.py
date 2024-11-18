
import requests
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2


def fetch_data():
    # URL API
    url = 'https://restcountries.com/v3.1/all'

    try:
        response = requests.get(url)

        if response.status_code == 200:
            users = response.json()

    except requests.exceptions.RequestException as err:
        print(f"Произошла ошибка при запросе: {err}")


# Замените следующие параметры на свои значения
username = 'onetwo'  # ваше имя пользователя
password = 'ffactory61'  # ваш пароль
host = 'localhost'  # адрес вашего сервера, может быть localhost
port = '5434'  # стандартный порт для PostgreSQL
database = 'pet_project'  # название вашей базы данных

# Строка подключения
DATABASE_URL = f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}'

# Создаем движок и базу данных
engine = create_engine(DATABASE_URL)
Base = declarative_base()


# Определяем модель таблицы
class Country(Base):
    __tablename__ = 'countries'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    capital = Column(String)
    currency = Column(String)
    population = Column(Integer)


# Создаем таблицы
Base.metadata.create_all(engine)


# Функция для вставки данных в базу данных
def insert_data(countries_data):
    Session = sessionmaker(bind=engine)
    session = Session()

    for country in countries_data:
        country_entry = Country(
            name=country.get('name'),
            capital=country.get('capital'),
            currency=country.get('currencies')[0].get('name') if 'currencies' in country and len(
                country['currencies']) > 0 else None,
            population=country.get('population')
        )
        session.add(country_entry)

    session.commit()
    session.close()

