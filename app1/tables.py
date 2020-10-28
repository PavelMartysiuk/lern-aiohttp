from sqlalchemy import (
    create_engine,
    DateTime,
    Integer,
    String,
    Column,
    Float,
    Table,
)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from datetime import datetime

from app1.settings import load_config

engine = create_engine(load_config()['sqlalchemy'])

Base = declarative_base()
Session = sessionmaker(bind=engine)


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    last__name = Column(String)
    email = Column(String)
    password = Column(String)
    add_date = Column(DateTime, default=datetime.now().strftime("%B %d, %Y"))


class Items(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)
if __name__  == '__main__':
    Base.metadata.create_all(engine)