from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from src.h14.model.book import Book
from src.h14.model.genre import Genre
from src.h14.model.order import Order
from src.h14.model.user import Human
from src.h14.manager.book import BookManager
from src.h14.manager.genre import GenreManager
from src.h14.user.genre import UserManager


engine = create_engine('sqlite:///nya.db', echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

while True:
    print("Menu:")
    print("[1] Create")
    print("[2] Add")
    print("[3] Read")
    print("[4] Modify")
    print("[5] Delete")
    print("[0] Exit")
    try:
        choice = int(input("Enter your choice: "))
        if choice == 0:
            break
        elif choice == 1:
            try:
                user_id = int(input('Enter user_id: '))
                book_id = int(input('Enter user_id: '))
                order = Order(user_id=user_id, book_id=book_id)
                user = session.query(Human).get(user_id)
                book = session.query(Book).get(book_id)
                if user and book:
                    if user.balance >= book.price:
                        user.balance -= book.price
                        session.commit()
                        print("Order created")
                    else:
                        print("Not enough balance")
                else:
                    print("User or book not found")
                if book:
                    if book.amount > 0:
                        book.amount -= 1
                        session.commit()
                    else:
                        print("You don't have any book")
                else:
                    print("Book not found")
            except Exception as e:
                print(e)
        elif choice == 2:
            while True:
                print("Menu:")
                print("[1] Add a user")
                print("[2] Add a book")
                print("[3] Add a genre")
                print("[0] Go back")
                try:
                    new_choice = input("Enter your choice: ")
                    if new_choice == 0:
                        break
                    elif choice == 1:
                        first_name = input('Enter first name: ')
                        last_name = input('Enter last name: ')
                        email = input('Enter email: ')
                        age = int(input('Enter age: '))
                        balance = float(input('Enter balance: '))
                        new_user = Human(first_name=first_name, last_name=last_name,
                                         email=email, age=age, balance=balance)
                        session.add(new_user)
                        session.commit()
                        print("User created")
                    elif choice == 2:
                        title = input('Enter title: ')
                        description = input('Enter description: ')
                        amount = int(input('Enter amount: '))
                        price = float(input('Enter price: '))
                        genre_id = int(input('Enter genre_id: '))
                        new_book = Book(title=title, description=description, amount=amount,
                                        price=price, genre_id=genre_id)
                        session.add(new_book)
                        session.commit()
                        print("Book added")
                    elif choice == 3:
                        name = input('Enter genre name: ')
                        new_genre = Genre(name=name)
                        session.add(new_genre)
                        session.commit()
                        print("Genre added")
                except Exception as e:
                    print(e)
        elif choice == 3:
            while True:
                print("Menu:")
                print("[1] View users")
                print("[2] View books")
                print("[3] View orders")
                print("[4] View genres")
                print("[0] Go back")
                try:
                    new_choice = input("Enter your choice: ")
                    if new_choice == 0:
                        break
                    elif new_choice == 1:
                        users = session.query(Human).scalars().all()
                        for user in users:
                            print(user.id, user.first_name, user.last_name, user.email)
                    elif new_choice == 2:
                        books = session.query(Book).scalars().all()
                        for book in books:
                            print(book.id, book.title, book.price)
                    elif new_choice == 3:
                        orders = session.query(Order).scalars().all()
                        for order in orders:
                            print(order.id, order.book_id, order.user_id)
                    elif new_choice == 4:
                        genres = session.query(Genre).scalars().all()
                        for genre in genres:
                            print(genre.id, genre.name)
                except Exception as e:
                    print(e)
        elif choice == 4:
            while True:
                print("Menu:")
                print("[1] Change user ")
                print("[2] Change book")
                print("[3] Change genre")
                print("[0] Go back")
                try:
                    new_choice = input("Enter your choice: ")
                    if new_choice == 0:
                        break
                    elif new_choice == 1:
                        try:
                            user_id = int(input('Enter user ID to update: '))
                            user_manager = UserManager()
                            user = user_manager.get_by_id(Human, user_id, session)
                            if user:
                                new_name = input('Enter new name: ')
                                new_value = input(f'Enter new value: ')
                                user_data = {new_name: new_value}
                                updated_user = user_manager.update(Human, user_id, user_data, session)
                            else:
                                print('User not found')
                        except Exception as e:
                            print(e)
                    elif new_choice == 2:
                        try:
                            book_id = int(input('Enter user ID to update: '))
                            book_manager = BookManager()
                            book = book_manager.get_by_id(Book, book_id, session)
                            if book:
                                new_title = input('Enter new title: ')
                                new_price = input(f'Enter new price: ')
                                book_data = {new_title: new_price}
                                updated_book = book_manager.update(Book, book_id, book_data, session)
                            else:
                                print('Book not found')
                        except Exception as e:
                            print(e)
                    elif new_choice == 3:
                        try:
                            genre_id = int(input('Enter user ID to update: '))
                            genre_manager = GenreManager()
                            genre = genre_manager.get_by_id(Genre, genre_id, session)
                            if genre:
                                new_genre = input('Enter genre: ')
                                genre_data = {'name': genre}
                                """принимает словарь, но от пользователя нужен только жанр. что делать?"""
                                updated_genre = genre_manager.update(Genre, genre_id, genre_data, session)
                            else:
                                print('Genre not found')
                        except Exception as e:
                            print(e)
                except Exception as e:
                    print(e)
        elif choice == 5:
            while True:
                print("Menu:")
                print("[1] Delete the user")
                print("[2] Delete book")
                print("[3] Delete genre")
                print("[0] Go back")
                try:
                    new_choice = input("Enter your choice: ")
                    if new_choice == 0:
                        break
                    elif new_choice == 1:
                        user_id = int(input('Enter user ID to delete: '))
                        user_manager = UserManager()
                        user = user_manager.get_by_id(Human, user_id, session)
                        if user:
                            user_manager.delete(Human, user_id, session)
                            print("User deleted")
                            break
                        else:
                            print("User not found")
                    elif new_choice == 2:
                        book_id = int(input('Enter book ID to delete: '))
                        book_manager = BookManager()
                        book = book_manager.get_by_id(Book, book_id, session)
                        if book:
                            book_manager.delete(Book, book_id, session)
                            print("Book deleted")
                        else:
                            print("Book not found")
                    elif new_choice == 3:
                        genre_id = int(input('Enter genre ID to delete: '))
                        genre_manager = GenreManager()
                        genre = genre_manager.get_by_id(Genre, genre_id, session)
                        if genre:
                            genre_manager.delete(Genre, genre_id, session)
                            print("Genre deleted")
                        else:
                            print("Genre not found")
                except Exception as e:
                    print(e)
    except Exception as e:
        print(e)
