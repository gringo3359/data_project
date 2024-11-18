from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


username = 'onetwo'
password = 'ffactory61'
host = 'localhost'
port = '5434'
database = 'pet_project'

DATABASE_URL = f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}'

engine = create_engine(DATABASE_URL)
Base = declarative_base()