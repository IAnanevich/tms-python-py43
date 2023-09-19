"""SQLAlchemy Data Models."""
from sqlalchemy import Column, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.types import Integer, SmallInteger, Float, Text, String, DateTime

from database import engine

Base = declarative_base()


# Base.metadata.drop_all(engine)
# Base.metadata.create_all(engine)

# 1) Человек (поля: id, first name: str, last_name: str, email: str, age: int, balance: float, created at, updated at)
class User(Base):  # type: ignore
    """User account."""
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement="auto")
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    age = Column(SmallInteger, nullable=True)
    balance = Column(Float, nullable=False, default=0)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now())


# 2) Книга (поля: id, title: str, description: text, amount: int, price: float, genre_id: int, created at, updated at)
class Book(Base):  # type: ignore
    """Book list"""
    __tablename__ = "book"
    id = Column(Integer, primary_key=True, autoincrement="auto")
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    amount = Column(SmallInteger, default=0)
    price = Column(Float, default=0)
    genre_id = Column(Integer, ForeignKey("genre.id"))
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now())
    genre = relationship("Genre", foreign_keys=[genre_id])


# 3) Заказ (поля: id, title_id: int, user_id: int, created at, updated at) - промежуточная для связи M2M между
# Человек и Девайс
class Order(Base):  # type: ignore
    """Order list"""
    __tablename__ = "order"
    id = Column(Integer, primary_key=True, autoincrement="auto")
    book_id = Column(Integer, ForeignKey("book.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    quantity = Column(Integer, nullable=False)  # add
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, server_default=func.now(), nullable=False)
    user = relationship("User", foreign_keys=[user_id])
    book = relationship("Book", foreign_keys=[book_id])


# 4) Жанр (поля: id, name: str, created at, updated at)
class Genre(Base):  # type: ignore
    """Genre list"""
    __tablename__ = "genre"
    id = Column(Integer, primary_key=True, autoincrement="auto")
    name = Column(String(30), nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, server_default=func.now(), nullable=False)


# Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
