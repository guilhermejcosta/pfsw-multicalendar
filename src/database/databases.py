from sqlalchemy.orm import scoped_session, sessionmaker, Session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
        
class MySQL:
    def __init__(self):
        self.user='application'
        self.password='applicationapi'
        self.host='mysql'
        self.port=3306
        self.database='multicalendar'
        self.dialect_driver='mysql+pymysql'
    def session(self):        
        engine = create_engine(f'{self.dialect_driver}://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}?charset=utf8mb4')
        session = Session(engine)
        return session
    def engine(self):
        return create_engine(f'{self.dialect_driver}://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}?charset=utf8mb4')