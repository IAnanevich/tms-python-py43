from models import Reader, Genre, Book, Order
from sqlalchemy.orm import Session
from sqlalchemy import update

session = Session()


def update_order():
    new_balance = update(Order).where(Order.user_id == id(input('Reader id: '))).values(
        balance=Reader.balance - Book.price
    )
    new_amount = update(Order).where(Order.book_id == id(input('Book id: '))).values(
        amount=-1
    )
    session.execute(new_balance)
    session.execute(new_amount)
    session.commit()


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
    s = update(Genre).where(Genre.pk == id(input("update genre by id: "))).values(
        name=str(input())
    )
    session.execute(s)
    session.commit()
    print(s)
