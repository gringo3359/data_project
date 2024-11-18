import random
import db_connection as dbcon
from datetime import datetime, timedelta
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

class Person(dbcon.Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    dob = Column(String)  # Форматирование даты в строку 'дд/мм/гггг'
    country_id = Column(Integer)

dbcon.Base.metadata.create_all(dbcon.engine)

def generate_random_name():
    first_names = ['John', 'Jane', 'Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Hannah']
    last_names = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor']
    return f"{random.choice(first_names)} {random.choice(last_names)}"

def generate_random_dob():
    start_date = datetime(1950, 1, 1)
    end_date = datetime(2005, 12, 31)
    random_days = random.randint(0, (end_date - start_date).days)
    dob = start_date + timedelta(days=random_days)
    return dob.strftime('%d/%m/%Y'), dob

def calculate_age(dob):
    dob_date = datetime.strptime(dob, '%d/%m/%Y')
    today = datetime.today()
    age = today.year - dob_date.year - ((today.month, today.day) < (dob_date.month, dob_date.day))
    return age

def add_people_to_db(session):
    id_counter = 1

    # Генерируем 75 записей с country_id от 1 до 15, по 5 записей на каждую страну
    for country_id in range(1, 16):
        for _ in range(5):
            name = generate_random_name()
            print('fergerg')
            dob, dob_date = generate_random_dob()
            age = calculate_age(dob)
            person = Person(id=id_counter, name=name, age=age, dob=dob, country_id=country_id)
            session.add(person)
            id_counter += 1

    # Замените строку подключения на вашу


    Session = sessionmaker(bind=dbcon.engine)
    session = Session()
    add_people_to_db(session)
    session.commit()
    session.close()