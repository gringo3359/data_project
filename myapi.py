
import requests
import db_connection as dbcon
from sqlalchemy import Column, Integer, String
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


class Country(dbcon.Base):
    __tablename__ = 'countries'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    capital = Column(String)
    currency = Column(String)
    population = Column(Integer)

dbcon.Base.metadata.create_all(dbcon.engine)


def insert_data(countries_data):
    Session = sessionmaker(bind=dbcon.engine)
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


