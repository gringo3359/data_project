from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

file_path = '/Users/onetwo/Downloads/pwd.txt'

with open(file_path, 'r') as file:
    pswd = file.readline().strip()


username = 'onetwo'
password = pswd
host = 'localhost'
port = '5434'
database = 'pet_project'

DATABASE_URL = f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}'

engine = create_engine(DATABASE_URL)
Base = declarative_base()