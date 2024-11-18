from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

file_path = '/Users/onetwo/Downloads/pwd.txt'

with open(file_path, 'r') as file:
    DATABASE_URL = file.readline().strip()

engine = create_engine(DATABASE_URL)
Base = declarative_base()