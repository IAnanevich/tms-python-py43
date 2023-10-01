from datetime import datetime

from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Float,
    DateTime,
    Text,
    ForeignKey,
)
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

Base = declarative_base()


# Человек - просто обычный пользователь
# 1) Человек (поля: id, first name: str, last_name: str, email: str, age: int, balance: float, created at, updated at)
class User(Base):
    """
    class of Users
    """

    __tablename__ = "users"
    id = Column("user_id", Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(20), nullable=False)
    last_name = Column(String(20), nullable=False)
    email = Column(String(20), nullable=False, unique=True)
    age = Column(Integer)
    balance = Column(Float, nullable=False)
    created_at = Column(DateTime(), default=datetime.now)
    updated_at = Column(DateTime(), default=datetime.now, onupdate=datetime.now)


# Книга - любая книга
# 2) Книга (поля: id, title: str, description: text, amount: int, price: float, genre_id: int, created at, updated at)
class Book(Base):
    """
    class of books
    """

    __tablename__ = "books"
    id = Column("book_id", Integer, primary_key=True, autoincrement=True)
    title = Column(String(20), nullable=False)
    description = Column(Text, nullable=False)
    amount = Column(Integer)
    price = Column(Float, nullable=False)
    genre_id = Column(Integer, ForeignKey("genres.genre_id"))
    created_at = Column(DateTime(), default=datetime.now)
    updated_at = Column(DateTime(), default=datetime.now, onupdate=datetime.now)
    genre_name = relationship("Genre")


# Заказ - человек заказывает книгу для покупки - промежуточная для связи M2M между Человек и Книга
# 3) Заказ (поля: id, title_id: int, user_id: int, created at, updated at) - для связи M2M между Человек и Девайс
class Order(Base):
    """
    class of orders
    """

    __tablename__ = "orders"
    id = Column("order_id", Integer, primary_key=True, autoincrement=True)
    title_id = Column(Integer, ForeignKey("books.book_id"))
    user_id = Column(Integer, ForeignKey("users.user_id"))
    created_at = Column(DateTime(), default=datetime.now)
    updated_at = Column(DateTime(), default=datetime.now, onupdate=datetime.now)
    user = relationship("User")
    book = relationship("Book")


# Жанр - содержит жанр книг (O2M с книгами), один жанр = много книг
# 4) Жанр (поля: id, name: str, created at, updated at)
class Genre(Base):
    """
    class of genres of books
    """

    __tablename__ = "genres"
    id = Column("genre_id", Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)
    created_at = Column(DateTime(), default=datetime.now)
    updated_at = Column(DateTime(), default=datetime.now, onupdate=datetime.now)


engine = create_engine("sqlite:///test_hw13.db", echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base.metadata.create_all(engine)
