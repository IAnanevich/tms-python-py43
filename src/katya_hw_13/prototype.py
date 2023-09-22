from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

engine = create_engine('sqlite:///bookshop.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()
Base.metadata.create_all(bind=engine)


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
    amount = Column(Integer, default=1, nullable=False)
    price = Column(Integer,  default=0, nullable=False)
    genre_id = Column('genre_id', Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime(), default=datetime.now)
    updated_at = Column(DateTime(), default=datetime.now, onupdate=datetime.now)
    genre = relationship("genres", foreign_keys=[genre_id])


class Order(Base):
    __tablename__ = 'orders'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    title_id = Column(Integer, ForeignKey('Books.id'))
    users_id = Column(Integer, ForeignKey('Users.id'))
    created_at = Column(DateTime(), default=datetime.now)
    updated_at = Column(DateTime(), default=datetime.now, onupdate=datetime.now)
    user = relationship("Users", foreign_keys=[users_id])
    book = relationship("Books", foreign_keys=[title_id])


class Genre(Base):
    __tablename__ = 'genres'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    created_at = Column(DateTime(), default=datetime.now)
    updated_at = Column(DateTime(), default=datetime.now, onupdate=datetime.now)
