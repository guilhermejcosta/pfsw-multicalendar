from sys import path
from os.path import join
from os import  getenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey, Integer, String, TIMESTAMP

Base = declarative_base()

path.append(join(getenv('APP_PATH')))

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    full_name = Column(String)
    display_name = Column(String)
    email = Column(String)
    contact_phone = Column(Integer)
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)
    deleted_at = Column(TIMESTAMP)