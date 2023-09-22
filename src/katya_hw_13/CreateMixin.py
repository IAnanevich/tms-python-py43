from sqlalchemy.orm import Session
from prototype import User, Book, Order, Genre
from ReadMixin import read_user, read_book, read_genre


def create_user(session: Session):
    """

    :param session:
    :return:
    """
    new_user = User()
    new_user.first_name = input('Введите ваше имя ')
    new_user.last_name = input('Введите вашу фамилию ')
    new_user.email = input('Введите ваш электронный адрес ')
    new_user.age = int(input('Введите ваш возраст '))
    new_user.balance = float(input('Ваша сумма на балансе составляет '))

    session.add(instance=new_user)
    session.commit()
    print(f'Новый пользователь {new_user.first_name} {new_user.last_name}')


def create_book(session: Session):
    """

    :param session:
    :return:
    """
    new_book = Book()
    read_genre(session=session)

    new_book.title = input('Введите название книги ')
    new_book.amount = int(input('Введите количество книг '))
    new_book.price = float(input('Введите стоимость книги '))
    new_book.genre_id = int(input('Введите id жанра книги '))

    session.add(instance=new_book)
    session.commit()
    print(f'Новая книга {new_book.title} в кол-ве {new_book.amount} по цене {new_book.price}')


def create_order(session: Session):
    """

    :param session:
    :return:
    """
    new_order = Order()

    read_user(session=session)
    new_order.human_id = int(input('ВВведите id покупателя '))

    read_book(session=session)
    new_order.book_id = int(input('Введите id книги '))

    book = session.query(Book).get(ident=new_order.book_id)
    book.amount -= 1
    user = session.query(User).get(ident=new_order.user_id)
    user.balance -= book.price

    session.add(instance=user)
    session.add(instance=book)
    session.add(instance=new_order)
    session.commit()
    print(f'Новый заказ {new_order.id}')


def create_genre(session: Session):
    """

    :param session:
    :return:
    """
    new_genre = Genre()
    new_genre.name = input('Введите название нового жанра ')

    session.add(instance=new_genre)
    session.commit()
    print(f'Новый жанр {new_genre.name}')
