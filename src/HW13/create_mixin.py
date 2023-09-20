from models import Reader, Genre, Book, Order, engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import update

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


def create_order():
    new_balance = update(Order).where(Order.user_id == id(input('Reader id: '))).values(
        balance=Reader.balance - Book.price
    )
    new_amount = update(Order).where(Order.book_id == id(input('Book id: '))).values(
        amount=-1
    )
    session.execute(new_balance)
    session.execute(new_amount)
    session.commit()
