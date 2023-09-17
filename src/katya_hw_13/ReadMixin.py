from sqlalchemy.orm import Session
from prototype import User, Book, Order, Genre


def read_user(session: Session):
    """

    :param session:
    :return:
    """
    for i in session.query(User).all():
        print(i.id, i.first_name, i.last_name, i.balance)


def read_book(session: Session):
    """

    :param session:
    :return:
    """
    for i in session.query(Book).all():
        print(i.id, i.title, i.genre_id, f'цена {i.price}', f'наличие {i.amount}')


def read_order(session: Session):
    """

    :param session:
    :return:
    """
    for i in session.query(Order).all():
        print(
            f'Пользователь {i.id}-{i.user.first_name}'
            f'сделал заказ {i.book.title} по цене {i.book.price}'
        )


def read_genre(session: Session):
    """

    :param session:
    :return:
    """
    for i in session.query(Genre).all():
        print(i.id, i.name)
