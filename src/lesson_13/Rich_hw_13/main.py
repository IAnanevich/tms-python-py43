from src.lesson_13.Rich_hw_13.db import session, Base, engine
from src.lesson_13.Rich_hw_13.managers.manager import BookManager
from src.lesson_13.Rich_hw_13.managers.manager import GenreManager
from src.lesson_13.Rich_hw_13.managers.manager import OrderManager
from src.lesson_13.Rich_hw_13.managers.manager import UserManager
from src.lesson_13.Rich_hw_13.menu import Menu
from src.lesson_13.Rich_hw_13.models.models import Book
from src.lesson_13.Rich_hw_13.models.models import Genre
from src.lesson_13.Rich_hw_13.models.models import Order
from src.lesson_13.Rich_hw_13.models.models import User

if __name__ == '__main__':

    Base.metadata.create_all(engine)

    while True:
        choice = Menu.main_menu()

        if choice == '1':
            book_id = int(input('Enter an book_id: '))
            user_id = int(input('Enter an user_id: '))

            input_data = {
                'user_id': user_id,
                'book_id': book_id,
            }
            order = OrderManager.create(table=Order, input_data=input_data, session=session)

            book = BookManager.get_by_id(table=Book, pk=book_id, session=session)
            new_book = BookManager.update(
                table=Book, pk=book_id, input_data={'amount': book.amount - 1}, session=session
            )

            user = UserManager.get_by_id(table=User, pk=user_id, session=session)
            new_user = UserManager.update(
                table=User, pk=user_id, input_data={'balance': user.balance - book.price}, session=session
            )

            print(f'New order: {order}')
            print(f'New user balance: {user.balance}')
            print(f'New book amount: {book.amount}')

        elif choice == '2':

            sub_choice = Menu.create_menu()

            if sub_choice == '1':
                input_data = {
                    'first_name': input('Enter first_name: '),
                    'last_name': input('Enter last_name: '),
                    'email': input('Enter email: '),
                    'age': int(input('Enter age: ')),
                    'balance': float(input('Enter balance: ')),
                }
                user = UserManager.create(table=User, input_data=input_data, session=session)
                print(f'User: {user.__dict__}')

            elif sub_choice == '2':
                input_data = {
                    'title': input('Enter title: '),
                    'description': input('Enter description: '),
                    'amount': int(input('Enter amount: ')),
                    'price': float(input('Enter price: ')),
                    'genre_id': int(input('Enter genre id: '))
                }
                book = BookManager.create(table=Book, input_data=input_data, session=session)
                print(f'Book: {book.__dict__}')

            elif sub_choice == '3':
                genre = GenreManager.create(table=Genre, input_data={'name': input('Enter name: ')}, session=session)
                print(f'Genre: {genre.__dict__}')

            elif sub_choice == '0':
                pass

            else:
                print('Try again')

        elif choice == '3':

            sub_choice = Menu.list_menu()

            if sub_choice == '1':
                users = UserManager.list(table=User, session=session)
                for user in users:
                    print(user.__dict__)

            elif sub_choice == '2':
                books = BookManager.list(table=Book, session=session)
                for book in books:
                    print(book.__dict__)

            elif sub_choice == '3':
                orders = OrderManager.list(table=Order, session=session)
                for order in orders:
                    print(order.__dict__)

            elif sub_choice == '4':
                genres = GenreManager.list(table=Genre, session=session)
                for genre in genres:
                    print(genre.__dict__)

            elif sub_choice == '0':
                pass

            else:
                print('Try again')

        elif choice == '4':

            sub_choice = Menu.update_menu()

            if sub_choice == '1':
                user_id = int(input('Enter user id: '))
                user = UserManager.get_by_id(table=User, pk=user_id, session=session)
                input_data = {
                    'first_name': input('Enter first_name: '),
                    'last_name': input('Enter last_name: '),
                    'email': input('Enter email: '),
                    'age': int(input('Enter age: ')),
                    'balance': float(input('Enter balance: ')),
                }
                new_user = UserManager.update(
                    table=User,
                    pk=user_id,
                    input_data=input_data,
                    session=session
                )
                print(new_user.__dict__)

            elif sub_choice == '2':
                book_id = int(input('Enter book id: '))
                book = BookManager.get_by_id(table=Book, pk=book_id, session=session)
                input_data = {
                    'title': input('Enter title: '),
                    'description': input('Enter description: '),
                    'amount': int(input('Enter amount: ')),
                    'price': float(input('Enter price: ')),
                }
                new_book = BookManager.update(
                    table=Book,
                    pk=book_id,
                    input_data=input_data,
                    session=session
                )
                print(new_book.__dict__)

            elif sub_choice == '3':
                genre_id = int(input('Enter genre id: '))
                genre = GenreManager.get_by_id(table=Genre, pk=genre_id, session=session)
                new_genre = BookManager.update(
                    table=Genre,
                    pk=genre_id,
                    input_data={'name': input('Enter name: ')},
                    session=session
                )
                print(new_genre.__dict__)

            elif sub_choice == '0':
                pass
            else:
                print('Try again')

        elif choice == '4':
            sub_choice = Menu.delete_menu()

            if sub_choice == '1':
                column_id = int(input('Enter user id: '))
                user = UserManager.get_by_id(table=User, pk=column_id, session=session)
                deleted = UserManager.delete(table=User, pk=column_id, session=session)
                print(deleted.__dict__)

            elif sub_choice == '2':
                column_id = int(input('Enter book id: '))
                book = BookManager.get_by_id(table=Book, pk=column_id, session=session)
                deleted = BookManager.delete(table=Book, pk=column_id, session=session)
                print(deleted.__dict__)

            elif sub_choice == '3':
                column_id = int(input('Enter genre id: '))
                genre = GenreManager.get_by_id(table=Genre, pk=column_id, session=session)
                deleted = GenreManager.delete(table=Genre, pk=column_id, session=session)
                print(deleted.__dict__)
