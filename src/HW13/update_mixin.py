from models import Reader, Genre, Book, Order, engine
from sqlalchemy.orm import sessionmaker
from create_mixin import create_reader, create_book, create_genre
from list_mixin import read_reader_table
from sqlalchemy import update

Session = sessionmaker(bind=engine)
session = Session()


def update_reader():
    s = update(Reader).where(Reader.id.pk == id(input("update reader by id: "))).values(
        first_name=str(input()),
        last_name=str(input()),
        email=str(input()),
        age=int(input()),
        balanse=float(input()),
    )
    session.execute(s)
    session.commit()
    print(s)


def update_book():
    s = update(Book).where(Book.id.pk == id(input("update book by id: "))).values(
        title=str(input()),
        description=str(input()),
        amount=int(input()),
        price=float(input()),
        genre_id=int(input()),
    )
    session.execute(s)
    session.commit()
    print(s)


def update_genre():
    s = update(Genre).where(Genre.id.pk == id(input("update genre by id: "))).values(
        name=str(input())
    )
    session.execute(s)
    session.commit()
    print(s)

# def update_order_minus():
#     s = update(Reader.balance).where(Book.price == int)
#
#
# def update_order_plus():
#     s = update(Reader.balance).where(Book.amount == int).values(
#
#     )
