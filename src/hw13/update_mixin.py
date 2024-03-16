from sqlalchemy.orm import Session
from model import Books, Genres, Humans, Orders
from read_mixin import read_humans, read_books, read_genres, read_orders


def update_order(session: Session):
    read_orders(session=session)
    obj = session.query(Orders).get(ident=int(input("Введите id для изменения: >>")))

    read_humans(session=session)
    obj.human_id = int(input("Введите id человека: >>"))

    read_books(session=session)
    obj.book_id = int(input("Введите id книги: >>"))

    curr_book = session.query(Humans).get(ident=obj.book_id)
    curr_book.amount += 1
    curr_human = session.query(Humans).get(ident=obj.human_id)
    curr_human.balance += curr_book.price

    book = session.query(Books).get(ident=obj.book_id)
    book.amount -= 1
    human = session.query(Humans).get(ident=obj.human_id)
    human.balance -= book.price

    session.add(obj)
    session.add(curr_human)
    session.add(curr_book)
    session.add(human)
    session.add(book)
    session.commit()
    print("Изменен заказ: ", obj.id)


def update_human(session: Session):
    read_humans(session=session)
    obj = session.query(Humans).get(ident=int(input("Введите id для изменения: >>")))
    obj.first_name = input("Введите имя: >>")
    obj.last_name = input("Введите фамилию: >>")
    obj.email = input("Введите почту: >>")
    obj.age = int(input("Введите возраст: >>"))
    obj.balance = float(input("Введите сумму на балансе: >>"))

    session.add(obj)
    session.commit()
    print("Изменен человек: ", obj.first_name, obj.last_name)


def update_genre(session: Session):
    read_genres(session=session)
    obj = session.query(Genres).get(ident=int(input("Введите id для изменения: >>")))
    obj.name = input("Введите название жанра: >>")

    session.add(obj)
    session.commit()
    print("Изменен жанр: ", obj.name)


def update_book(session: Session):
    read_books(session=session)
    obj = session.query(Books).get(ident=int(input("Введите id для изменения: >>")))
    obj.genre_id = int(input("Введите id жанра: >>"))
    obj.title = input("Введите название книги: >>")
    obj.description = input("Введите описание книги: >>")
    obj.amount = int(input("Введите количество книг: >>"))
    obj.price = float(input("Введите цену книги: >>"))

    session.add(obj)
    session.commit()
    print("Изменена книга: ", obj.title, obj.amount, obj.price)
