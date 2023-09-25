from sqlalchemy import Column, ForeignKey
from sqlalchemy import String, Text, DateTime, Integer, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from ..base import Base


class BaseModel(Base):
    __abstract__ = True
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    created_at = Column('created_at', DateTime, default=datetime.now)
    updated_at = Column('updated_at', DateTime, default=datetime.now, onupdate=datetime.now)


class User(BaseModel):
    __tablename__ = 'users'
    first_name = Column('first_name', String(30), nullable=False)
    last_name = Column('last_name', String(30), nullable=False)
    email = Column('email', String(50), unique=True, nullable=False)
    age = Column('age', Integer, nullable=False)
    balance = Column('balance', Float, default=0, nullable=False)


class Book(BaseModel):
    __tablename__ = 'books'
    title = Column('title', String(50), nullable=False)
    description = Column('description', Text(100))
    amount = Column('amount', Integer, nullable=False, default=1)
    price = Column('price', Float, nullable=False, default=0)
    genre_id = Column('genre_id', Integer, ForeignKey('genres.id'))
    genre = relationship('Genre', foreign_keys=[genre_id])


class Order(BaseModel):
    __tablename__ = 'orders'
    title_id = Column('title_id', Integer, ForeignKey('books.id'), nullable=False)
    user_id = Column('user_id', Integer, ForeignKey('users.id'), nullable=False)
    user = relationship("User", foreign_keys=[user_id])
    book = relationship("Book", foreign_keys=[title_id])


class Genre(BaseModel):
    __tablename__ = 'genres'
    name = Column(String(30), nullable=False)
