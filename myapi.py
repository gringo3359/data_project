
import requests
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2


def fetch_data():

    url = 'https://restcountries.com/v3.1/all'

    try:
        response = requests.get(url)

        if response.status_code == 200:
            users = response.json()

    except requests.exceptions.RequestException as err:
        print(f"Произошла ошибка при запросе: {err}")



username = 'onetwo'
password = 'ffactory61'
host = 'localhost'
port = '5434'
database = 'pet_project'

DATABASE_URL = f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}'

engine = create_engine(DATABASE_URL)
Base = declarative_base()


class Country(Base):
    __tablename__ = 'countries'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    capital = Column(String)
    currency = Column(String)
    population = Column(Integer)


Base.metadata.create_all(engine)


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

