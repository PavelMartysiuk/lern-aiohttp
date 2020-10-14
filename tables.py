from sqlalchemy import create_engine, Integer, String, DateTime, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from sqlalchemy_serializer import SerializerMixin

engine = create_engine('postgresql://racoon:pass123@localhost/task2', )

Base = declarative_base()
Session = sessionmaker(bind=engine)


class User(Base, SerializerMixin):
    __tablename__ = 'users'

    serialize_rules = ('-id',)

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, unique=True)
    user_name = Column(String)
    last_user_name = Column(String)
    add_time = Column(DateTime, default=datetime.now())


Base.metadata.create_all(engine)
