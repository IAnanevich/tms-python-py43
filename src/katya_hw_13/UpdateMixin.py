from sqlalchemy.orm import Session
from prototype import User, Book, Order, Genre
from ReadMixin import read_user, read_book, read_order, read_genre


def update_user(session: Session):
    read_user(session=session)

    upd_user = session.query(User).get(ident=int(input('Введите id пользователя для редактирования  ')))
    upd_user.first_name = input('Введите новое имя ')
    upd_user.last_name = input('Введите новую фамилию ')
    upd_user.email = input('Введите новый электронный адрес ')
    upd_user.age = int(input('Введите новый возраст '))
    upd_user.balance = float(input('Введите новую сумму на балансе '))

    session.add(upd_user)
    session.commit()
    print(f'Позьзователь {upd_user.last_name} {upd_user.first_name} отредактирован')


def update_book(session: Session):
    read_book(session=session)
    upd_book = session.query(Book).get(ident=int(input('Введите id книги для редатирования ')))

    upd_book.title = input('Введите новое название книги ')
    upd_book.amount = int(input('Введите новое количество книг '))
    upd_book.price = float(input('Введите новую стоимость книги '))
    upd_book.genre_id = int(input('Введите новое id жанра '))

    session.add(upd_book)
    session.commit()
    print(f'Книга  {upd_book.title}, в кол-ве {upd_book.amount} по цене {upd_book.price} отредактирована ')


def update_order(session: Session):
    read_order(session=session)
    upd_order = session.query(Order).get(ident=int(input('Введите id заказа для редактирования ')))

    read_user(session=session)
    upd_order._id = int(input('Введите id пользователя для редактирования '))

    read_book(session=session)
    upd_order.book_id = int(input('Введите id книги для редактирования '))

    correct_book = session.query(User).get(ident=upd_order.book_id)
    correct_book.amount += 1
    correct_user = session.query(User).get(ident=upd_order.user_id)
    correct_user.balance += correct_book.price

    book = session.query(Book).get(ident=upd_order.book_id)
    book.amount -= 1
    user = session.query(User).get(ident=upd_order.user_id)
    user.balance -= book.price

    session.add(upd_order)
    session.add(correct_user)
    session.add(correct_book)
    session.add(user)
    session.add(book)
    session.commit()
    print(f'отредактированный заказ {upd_order.id}')


def update_genre(session: Session):
    read_genre(session=session)
    upd_genre = session.query(Genre).get(ident=int(input('Введите id жанра для редактирования ')))
    upd_genre.name = input('Введите новое название жанра ')

    session.add(upd_genre)
    session.commit()
    print(f'Отредактированный жанр {upd_genre.name}')
