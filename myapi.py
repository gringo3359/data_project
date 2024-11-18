
import requests
from sqlalchemy import create_engine, Column, Integer, String, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker



def fetch_data() -> list:

    url = 'https://restcountries.com/v3.1/all'

    try:
        response = requests.get(url)

        if response.status_code == 200:
            countries_data = response.json()

    except requests.exceptions.RequestException as err:
        print(f"Произошла ошибка при запросе: {err}")

    return countries_data



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
        curr = country['currencies'] if 'currencies' in country else None
        country_name = country['name']

        country_entry = Country(
            name=country_name.get('common'),
            capital=country['capital'][0] if 'capital' in country else None,
            currency=[name['name'] for name in curr.values()][0] if curr is not None else None,
            population=country.get('population')
        )
        session.add(country_entry)

    session.commit()
    session.close()


