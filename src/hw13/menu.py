from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import Base
from managers import UserManager, BookManager, OrderManager, GenreManager

# Подключение к базе данных
db_url = "sqlite:///my_database.db"
engine = create_engine(db_url)
Base.metadata.create_all(engine)
session = Session(engine)

# Инициализация менеджеров
user_manager = UserManager(session)
book_manager = BookManager(session)
order_manager = OrderManager(session)
genre_manager = GenreManager(session)

def main_menu():
    while True:
        print("Главное меню:")
        print("1. Сделать заказ")
        print("2. Добавить")
        print("3. Прочитать")
        print("4. Изменить")
        print("5. Удалить")
        print("0. Выйти")
        choice = input("Выберите действие: ")

        if choice == "1":
            make_order()
        elif choice == "2":
            add_menu()
        elif choice == "3":
            read_menu()
        elif choice == "4":
            update_menu()
        elif choice == "5":
            delete_menu()
        elif choice == "0":
            session.close()
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите снова.")

def add_menu():
    while True:
        print("Меню добавления:")
        print("1. Добавить пользователя")
        print("2. Добавить книгу")
        print("3. Добавить жанр")
        print("0. Вернуться назад")
        choice = input("Выберите действие: ")

        if choice == "1":
            add_user()
        elif choice == "2":
            add_book()
        elif choice == "3":
            add_genre()
        elif choice == "0":
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите снова.")

def read_menu():
    while True:
        print("Меню просмотра:")
        print("1. Посмотреть пользователей")
        print("2. Посмотреть книги")
        print("3. Посмотреть заказы")
        print("4. Посмотреть жанры")
        print("0. Вернуться назад")
        choice = input("Выберите действие: ")

        if choice == "1":
            print_users()
        elif choice == "2":
            print_books()
        elif choice == "3":
            print_orders()
        elif choice == "4":
            print_genres()
        elif choice == "0":
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите снова.")

def update_menu():
    while True:
        print("Меню изменения:")
        print("1. Изменить пользователя")
        print("2. Изменить книгу")
        print("3. Изменить жанр")
        print("0. Вернуться назад")
        choice = input("Выберите действие: ")

        if choice == "1":
            update_user()
        elif choice == "2":
            update_book()
        elif choice == "3":
            update_genre()
        elif choice == "0":
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите снова.")

def delete_menu():
    while True:
        print("Меню удаления:")
        print("1. Удалить пользователя")
        print("2. Удалить книгу")
        print("3. Удалить жанр")
        print("0. Вернуться назад")
        choice = input("Выберите действие: ")

        if choice == "1":
            delete_user()
        elif choice == "2":
            delete_book()
        elif choice == "3":
            delete_genre()
        elif choice == "0":
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите снова.")


def make_order():
    print("Сделать заказ")
    user_id = int(input("Введите ID пользователя: "))
    book_id = int(input("Введите ID книги: "))

    user = user_manager.get_person_by_id(user_id)
    book = book_manager.get_book_by_id(book_id)

    if user and book:
        if user.balance >= book.price and book.amount > 0:
            order_manager.create_order(title_id=book_id, user_id=user_id)
            user_manager.update_balance(user_id, user.balance - book.price)
            book_manager.update_book_quantity(book_id, book.amount - 1)
            print("Заказ успешно создан.")
        else:
            print("У пользователя недостаточно средств или нет доступных копий книги.")
    else:
        print("Пользователь или книга не найдены.")


def add_user():
    print("Добавить пользователя")
    first_name = input("Введите имя: ")
    last_name = input("Введите фамилию: ")
    email = input("Введите email: ")
    age = int(input("Введите возраст: "))
    balance = float(input("Введите баланс: "))

    user_manager.create_person(first_name, last_name, email, age, balance)
    print("Пользователь успешно добавлен.")


def add_book():
    print("Добавить книгу")
    title = input("Введите название книги: ")
    description = input("Введите описание: ")
    amount = int(input("Введите количество книг: "))
    price = float(input("Введите цену: "))
    genre_id = int(input("Введите ID жанра: "))

    book_manager.create_book(title, description, amount, price, genre_id)
    print("Книга успешно добавлена.")


def add_genre():
    print("Добавить жанр")
    name = input("Введите название жанра: ")

    genre_manager.create_genre(name)
    print("Жанр успешно добавлен.")

def print_users():
    print("Список пользователей:")
    users = user_manager.get_all_people()
    for user in users:
        print(f"ID: {user.id}, Имя: {user.first_name}, Фамилия: {user.last_name}, Email: {user.email}, Возраст: {user.age}, Баланс: {user.balance}")

def print_books():
    print("Список книг:")
    books = book_manager.get_all_books()
    for book in books:
        print(f"ID: {book.id}, Название: {book.title}, Описание: {book.description}, Количество: {book.amount}, Цена: {book.price}, Жанр: {book.genre.name}")

def print_orders():
    print("Список заказов:")
    orders = order_manager.get_all_orders()
    for order in orders:
        print(f"ID: {order.id}, Книга: {order.book.title}, Пользователь: {order.user.first_name} {order.user.last_name}")

def print_genres():
    print("Список жанров:")
    genres = genre_manager.get_all_genres()
    for genre in genres:
        print(f"ID: {genre.id}, Название: {genre.name}")

def update_user():
    print("Изменить пользователя")
    user_id = int(input("Введите ID пользователя для изменения: "))
    new_balance = float(input("Введите новый баланс: "))

    user_manager.update_balance(user_id, new_balance)
    print("Баланс пользователя успешно обновлен.")

def update_book():
    print("Изменить книгу")
    book_id = int(input("Введите ID книги для изменения: "))
    new_quantity = int(input("Введите новое количество книг: "))

    book_manager.update_book_quantity(book_id, new_quantity)
    print("Количество книг успешно обновлено.")

def update_genre():
    print("Изменить жанр")
    genre_id = int(input("Введите ID жанра для изменения: "))
    new_name = input("Введите новое название жанра: ")

    genre_manager.update_genre_name(genre_id, new_name)
    print("Название жанра успешно обновлено.")

def delete_user():
    print("Удалить пользователя")
    user_id = int(input("Введите ID пользователя для удаления: "))

    user_manager.delete_person(user_id)
    print("Пользователь успешно удален.")

def delete_book():
    print("Удалить книгу")
    book_id = int(input("Введите ID книги для удаления: "))

    book_manager.delete_book(book_id)
    print("Книга успешно удалена.")

def delete_genre():
    print("Удалить жанр")
    genre_id = int(input("Введите ID жанра для удаления: "))

    genre_manager.delete_genre(genre_id)
    print("Жанр успешно удален.")

if __name__ == "__main__":
    main_menu()