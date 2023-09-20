from sqlalchemy.orm import Session
from model import Books, Genres, Humans, Orders
from ReadMixin import read_humans, read_books, read_genres, read_orders


def delete_order(session: Session):
    # Конструктор удаления
    read_orders(session=session)
    obj = session.query(Orders).get(ident=int(input("Введите id для удаления: >>")))

    # Изменение баланса, вернем
    curr_human = session.query(Humans).get(ident=obj.human_id)
    curr_human.balance += obj.book.price

    # Запись
    session.add(curr_human)
    session.delete(obj)
    session.commit()


def delete_human(session: Session):
    # Конструктор удаления
    read_humans(session=session)
    obj = session.query(Humans).get(ident=int(input("Введите id для удаления: >>")))

    # Проверка
    result = session.query(Orders).filter(Orders.human_id == obj.id)
    for _ in result:
        print("Невозможно удалить человека, у него есть заказы!")
        return

    # Запись
    session.delete(obj)
    session.commit()


def delete_genre(session: Session):
    # Конструктор удаления
    read_genres(session=session)
    obj = session.query(Genres).get(ident=int(input("Введите id для удаления: >>")))

    # Проверка
    result = session.query(Books).filter(Books.genre_id == obj.id)
    for _ in result:
        print("Невозможно удалить жанр, у него есть книги!")
        return

    # Запись
    session.delete(obj)
    session.commit()


def delete_book(session: Session):
    # Конструктор удаления
    read_books(session=session)
    obj = session.query(Books).get(ident=int(input("Введите id для удаления: >>")))

    # Проверка
    result = session.query(Orders).filter(Orders.book_id == obj.id)
    for _ in result:
        print("Невозможно удалить книгу, у неё есть заказы!")
        return

    # Запись
    session.delete(obj)
    session.commit()
