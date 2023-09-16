from sqlalchemy.orm import Session
from model import Books, Genres, Humans, Orders


def read_orders(session: Session):
    # Конструктор чтения
    for i in session.query(Orders).all():
        print(f"Заказ {i.id}:", f"{i.human.first_name} заказал книгу '{i.book.title}' по цене: {i.book.price}")
    print("=" * 25)


def read_humans(session: Session):
    # Конструктор чтения
    for i in session.query(Humans).all():
        print(i.id, i.first_name, i.last_name, f"баланс: {i.balance}")
    print("=" * 25)


def read_genres(session: Session):
    # Конструктор чтения
    for i in session.query(Genres).all():
        print(i.id, i.name)
    print("=" * 25)


def read_books(session: Session):
    # Конструктор чтения
    for i in session.query(Books).all():
        print(i.id, i.title, i.genre.name, f"цена: {i.price}", f"доступно: {i.amount}")
    print("=" * 25)
