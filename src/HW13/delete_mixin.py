from models import Reader, Genre, Book, Order, engine
from sqlalchemy.orm import sessionmaker
from create_mixin import create_reader, create_book, create_genre
from list_mixin import read_reader_table
from sqlalchemy import delete

Session = sessionmaker(bind=engine)
session = Session()


def delete_reader():
    s = delete(Reader).where(Reader.id.pk == id(input("delete reader by id: ")))
    session.execute(s)
    session.commit()


def delete_book():
    s = delete(Book).where(Book.id.pk == id(input("delete book by id: ")))
    session.execute(s)
    session.commit()


def delete_genre():
    s = delete(Genre).where(Genre.id.pk == id(input("delete genre by id: ")))
    session.execute(s)
    session.commit()


def delete_order():
    s = delete(Genre).where(Order.id.pk == id(input("delete order by id: ")))
    session.execute(s)
    session.commit()
