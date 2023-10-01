from sqlalchemy.orm import Session
from elements_file import User, Book, Order, Genre
from read_file import read_users, read_books, read_orders, read_genres


def delete_user(session: Session) -> None:
    """
    delete user by ID
    :param session: current session
    :return: None
    """
    read_users(session=session)
    pk = int(input("Enter users ID to delete: "))
    obj = session.query(User).get(ident=pk)
    session.delete(obj)
    session.commit()


def delete_book(session: Session) -> None:
    """
    delete book by ID
    :param session: current session
    :return: None
    """
    read_books(session=session)
    pk = int(input("Enter ID of books to delete: "))
    obj = session.query(Book).get(ident=pk)
    session.delete(obj)
    session.commit()


def delete_order(session: Session) -> None:
    """
    delete order by ID
    :param session: current session
    :return: None
    """
    read_orders(session=session)
    pk = int(input("Enter ID of order to delete: "))
    obj = session.query(Order).get(ident=pk)
    session.delete(obj)
    session.commit()


def delete_genre(session: Session) -> None:
    """
    delete genre by ID
    :param session: current session
    :return: None
    """
    read_genres(session=session)
    pk = int(input("Enter ID of genre to delete: "))
    obj = session.query(Genre).get(ident=pk)
    session.delete(obj)
    session.commit()
