from sqlalchemy.orm import Session
from model import Books, Genres, Humans, Orders
from read_mixin import read_humans, read_books, read_genres


def create_order(session: Session):
    new_order = Orders()

    read_humans(session=session)
    new_order.human_id = int(input("Введите id человека: >>"))

    read_books(session=session)
    new_order.book_id = int(input("Введите id книги: >>"))

    book = session.query(Books).get(ident=new_order.book_id)
    book.amount -= 1
    human = session.query(Humans).get(ident=new_order.human_id)
    human.balance -= book.price

    session.add(instance=new_order)
    session.add(instance=human)
    session.add(instance=book)
    session.commit()
    print("Создан новый заказ: ", new_order.id)


def create_human(session: Session):
    new_human = Humans()
    new_human.first_name = input("Введите имя: >>")
    new_human.last_name = input("Введите фамилию: >>")
    new_human.email = input("Введите почту: >>")
    new_human.age = int(input("Введите возраст: >>"))
    new_human.balance = float(input("Введите сумму на балансе: >>"))

    session.add(instance=new_human)
    session.commit()
    print("Создан новый человек: ", new_human.first_name, new_human.last_name)


def create_genre(session: Session):
    new_genre = Genres()
    new_genre.name = input("Введите название нового жанра: >>")

    session.add(instance=new_genre)
    session.commit()
    print("Создан новый жанр: ", new_genre.name)


def create_book(session: Session):
    new_book = Books()

    read_genres(session=session)
    new_book.genre_id = int(input("Введите id жанра: >>"))
    new_book.title = input("Введите название книги: >>")
    new_book.description = input("Введите описание книги: >>")
    new_book.amount = int(input("Введите количество книг: >>"))
    new_book.price = float(input("Введите цену книги: >>"))

    session.add(instance=new_book)
    session.commit()
    print("Создана новая книга: ", new_book.title, new_book.amount, new_book.price)
