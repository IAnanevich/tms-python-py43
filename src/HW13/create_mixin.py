from models import Reader, Genre, Book, Order, engine
from sqlalchemy.orm import sessionmaker
from list_mixin import read_book_table, read_reader_table
from sqlalchemy import insert

Session = sessionmaker(bind=engine)
session = Session()


def create_reader():
    r1 = Reader(
        first_name=str(input()),
        last_name=str(input()),
        email=str(input()),
        age=int(input()),
        balance=float(input()),
    )
    session.add_all([r1])
    session.commit()


def create_book():
    b1 = Book(
        title=str(input()),
        description=str(input()),
        amount=int(input()),
        price=float(input()),
        genre_id=int(input()),
    )
    session.add_all([b1])
    session.commit()


def create_genre():
    g1 = Genre(
        name=str(input()),
    )
    session.add_all([g1])
    session.commit()

# def order_create():
