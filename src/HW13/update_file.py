from sqlalchemy.orm import Session

from elements_file import User, Book, Genre
from read_file import read_books, read_genres, read_users


def update_user(session: Session) -> None:
    """
    update user
    :param session: currently session
    :return: None
    """
    read_users(session=session)
    pk = int(input("Enter users ID to update: "))
    print("enter ID", pk)
    obj = session.query(User).get(ident=pk)
    obj.first_name = input("Enter new users first name: ")
    obj.last_name = input("Enter new users last name: ")
    obj.email = input("Enter new users email: ")
    obj.age = int(input("Enter new users age(will be an integer number): "))
    obj.balance = float(input("Enter new users balance(will be a float number): "))
    session.add(obj)
    session.commit()


def update_genre(session: Session) -> None:
    """
    update genre
    :param session: currently session
    :return: None
    """
    read_genres(session=session)
    pk = int(input("Enter ID of genre to update: "))
    obj = session.query(Genre).get(ident=pk)
    obj.name = input("Enter new name of genre: ")
    session.add(obj)
    session.commit()


def update_book(session: Session) -> None:
    """
    update user
    :param session: currently session
    :return: None
    """
    read_books(session=session)
    pk = int(input("Enter users ID to update: "))
    obj = session.query(Book).get(ident=pk)
    obj.title = input("Enter new title of book: ")
    obj.description = input("Enter new description of book: ")
    obj.amount = int(
        input("Enter new amount of book of the store(will be an integer number): ")
    )
    obj.price = float(input("Enter new price of book(will be a float number): "))
    obj.genre_id = int(input("Enter new id genre of book(will be an integer number): "))
    session.add(obj)
    session.commit()
