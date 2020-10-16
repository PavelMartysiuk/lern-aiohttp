from sqlalchemy import (
    create_engine,
    DateTime,
    MetaData,
    Integer,
    String,
    Column,
    Float,
    Table,
    Text
)

from datetime import datetime

from app1.settings import load_config

engine = create_engine(load_config()['sqlalchemy'])

metadata = MetaData()

users = Table(
    "users", metadata,
    Column("id", Integer, primary_key=True),
    Column("user_id", Integer, unique=True),
    Column("user_name", String),
    Column("last_user_name", Text),
    Column("add_time", DateTime, default=datetime.now())
)

items = Table(
    'items', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('price', Float)
)

metadata.create_all(engine)
