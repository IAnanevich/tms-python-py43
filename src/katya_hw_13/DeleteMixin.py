from sqlalchemy.orm import Session
from prototype import User, Book, Order, Genre
from ReadMixin import read_user, read_book, read_order, read_genre


def delete_user(session: Session):
    """

    :param session:
    :return:
    """
    read_user(session=session)
    del_user = session.query(User).get(ident=int(input('Введите id удаляемого пользователя ')))

    session.delete(del_user)
    session.commit()


def delete_book(session: Session):
    """

    :param session:
    :return:
    """
    read_book(session=session)
    del_book = session.query(Book).get(ident=int(input('Введите id удаляемой книги ')))

    session.delete(del_book)
    session.commit()


def delete_order(session: Session):
    """

    :param session:
    :return:
    """
    read_order(session=session)
    del_order = session.query(Order).get(ident=int(input('Введите id удаляемого заказа ')))

    correct_user = session.query(User).get(ident=del_order.user_id)
    correct_user.balance += del_order.book.price

    session.add(correct_user)
    session.delete(del_order)
    session.commit()


def delete_genre(session: Session):
    """

    :param session:
    :return:
    """
    read_genre(session=session)
    del_genre = session.query(Genre).get(ident=int(input('Введите id удаляемого жанра ')))

    session.delete(del_genre)
    session.commit()
