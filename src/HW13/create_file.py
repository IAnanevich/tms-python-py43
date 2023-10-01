from sqlalchemy.orm import Session
from elements_file import User, Book, Order, Genre
from read_file import read_users, read_books


def create_user(session: Session) -> None:
    """
    join new user to table 'users'
    :param session: currently session
    :return: None
    """
    # создание нового пользователя
    try:
        new_user = User(
            first_name=input("Enter users first name: "),
            last_name=input("Enter users last name: "),
            email=input("Enter users email: "),
            age=int(input("Enter users age(will be an integer number): ")),
            balance=float(input("Enter users balance(will be a float number): ")),
        )
    except ValueError as error:
        print(error)
    else:
        # добавление пользователя в базу при условии правильного ввода
        session.add(instance=new_user)
        session.commit()


def create_book(session: Session) -> None:
    """
    join new book to table 'books'
    :param session: currently session
    :return: None
    """
    # создание новой книги
    try:
        new_book = Book(
            title=input("Enter title of book: "),
            description=input("Enter description of book: "),
            amount=int(
                input("Enter amount of book of the store(will be an integer number): ")
            ),
            price=float(input("Enter price of book(will be a float number): ")),
            genre_id=int(input("Enter id genre of book(will be an integer number): ")),
        )
    except ValueError as error:
        print(error)
    else:
        # добавление книги в базу
        session.add(instance=new_book)
        session.commit()


def create_order(session: Session) -> None:
    """
    create new order to table 'orders'
    :param session: currently session
    :return: None
    """
    new_order = Order()
    print("Who want to make order?")
    read_users(session=session)
    new_order.user_id = int(input("Enter users ID fo order: "))
    print("Which book you want?")
    read_books(session=session)
    new_order.title_id = int(input("Enter ID of book to order: "))

    # уменьшаем количество книг на 1
    book = session.query(Book).get(ident=new_order.title_id)
    book.amount -= 1
    # уменьшаем баланс пользователя на стоимость книги
    us = session.query(User).get(ident=new_order.user_id)
    us.balance -= book.price

    session.add(book)
    session.add(us)
    session.add(new_order)
    session.commit()


def create_genre(session: Session) -> None:
    """
    join new genre to table 'genres'
    :param session: currently session
    :return: None
    """
    # создание нового жанра
    try:
        new_genre = Genre(name=input("Enter genre of book: "))
    except ValueError as error:
        print(error)
    else:
        # добавление жанра в базу
        session.add(instance=new_genre)
        session.commit()
