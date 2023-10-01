from sqlalchemy.orm import Session
from elements_file import User, Book, Order, Genre


def read_users(session: Session) -> None:
    """
    read base of users
    :param session: currently session
    :return: None
    """
    for rec in session.query(User).all():
        print(rec.id, rec.first_name, rec.last_name, rec.email, rec.age, rec.balance)


def read_books(session: Session) -> None:
    """
    read base of books
    :param session: currently session
    :return: None
    """
    for rec in session.query(Book).all():
        print(rec.id, rec.title, rec.description, rec.amount, rec.price, rec.genre_id)


def read_orders(session: Session) -> None:
    """
    read base of orders
    :param session: currently session
    :return: None
    """
    for rec in session.query(Order).all():
        print(rec.id, rec.title_id, rec.user_id)


def read_genres(session: Session) -> None:
    """
    read base of genres
    :param session: currently session
    :return: None
    """
    for rec in session.query(Genre).all():
        print(rec.id, rec.name)
