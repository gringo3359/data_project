
import requests
import sqlalchemy


def fetch_data():
    # URL API
    url = 'https://restcountries.com/v3.1/all'

    try:
        response = requests.get(url)

        if response.status_code == 200:
            users = response.json()

    except requests.exceptions.RequestException as err:
        print(f"Произошла ошибка при запросе: {err}")

    print(users)


fetch_data()