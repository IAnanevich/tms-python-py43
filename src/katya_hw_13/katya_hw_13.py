import datetime
from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime, SmallInteger, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

engine = create_engine('sqlite:///test.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class User(Base):  # model
    __tablename__ = 'users'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(20), nullable=False)
    last_name = Column(String(20), nullable=False)
    email = Column(String(20), nullable=False, unique=True)
    age = Column(Integer)
    balance = Column(Integer)
    created_at = Column(DateTime(), default=datetime.now)
    updated_at = Column(DateTime(), default=datetime.now, onupdate=datetime.now)

class Book(Base):
    __tablename__ = 'books'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    title = Column(String(100), nullable=False)
    amount = Column(Integer)
    price = Column(Integer)
    genre_id = Column('genre_id', Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime(), default=datetime.now)
    updated_at = Column(DateTime(), default=datetime.now, onupdate=datetime.now)

class Order(Base):
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    title_id = Column(String(100), nullable=False)
    users_id = relationship(User, backref='group')
    created_at = Column(DateTime(), default=datetime.now)
    updated_at = Column(DateTime(), default=datetime.now, onupdate=datetime.now)

class Genre(Base):
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False, ForeignKey('denre_id'))
    created_at = Column(DateTime(), default=datetime.now)
    updated_at = Column(DateTime(), default=datetime.now, onupdate=datetime.now)

while True:
    print(
        '1: Сделать заказ/n'
        '2: Добавить/n'
        '3: Прочитать/n'
        '4: Изменить/n'
        '5: Сделать заказ/n' 
    )
