from sqlalchemy import create_engine, Column, Integer, String, Text, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class BaseModel(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class Person(BaseModel):
    __tablename__ = 'person'
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    age = Column(Integer)
    balance = Column(Float)
    orders = relationship('Order', back_populates='user')

class Book(BaseModel):
    __tablename__ = 'book'
    title = Column(String(100), nullable=False)
    description = Column(Text)
    amount = Column(Integer, default=0)
    price = Column(Float, nullable=False)
    genre_id = Column(Integer, ForeignKey('genre.id'))

    genre = relationship("Genre", back_populates="books")


class Order(BaseModel):
    __tablename__ = 'order'
    title_id = Column(Integer, ForeignKey('book.id'))
    user_id = Column(Integer, ForeignKey('person.id'))

    user = relationship("Person", back_populates="orders")
    book = relationship("Book", back_populates="orders")


class Genre(BaseModel):
    __tablename__ = 'genre'
    name = Column(String(50), nullable=False, unique=True)

    books = relationship("Book", back_populates="genre")