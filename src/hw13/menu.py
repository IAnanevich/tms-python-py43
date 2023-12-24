from sqlalchemy.orm import Session
from create_mixin import create_human, create_book, create_genre, create_order
from read_mixin import read_humans, read_books, read_genres, read_orders
from delete_mixin import delete_human, delete_book, delete_genre, delete_order
from update_mixin import update_human, update_book, update_genre, update_order


class Menu:

    @classmethod
    def draw_menu(cls, menu_name: str) -> None:

        if menu_name == "Главное":
            print("1. Добавить")
            print("2. Прочитать")
            print("3. Изменить")
            print("4. Удалить")
            print("0. Выйти")

        if menu_name == "Добавить":
            print("1. Добавить человека")
            print("2. Добавить книгу")
            print("3. Добавить жанр")
            print("4. Добавить заказ")
            print("0. Выйти")

        if menu_name == "Прочитать":
            print("1. Посмотреть человек")
            print("2. Посмотреть книги")
            print("3. Посмотреть жанры")
            print("4. Посмотреть заказы")
            print("0. Выйти")

        if menu_name == "Изменить":
            print("1. Изменить человека")
            print("2. Изменить книгу")
            print("3. Изменить жанр")
            print("4. Изменить заказ")
            print("0. Выйти")

        if menu_name == "Удалить":
            print("1. Удалить человека")
            print("2. Удалить книгу")
            print("3. Удалить жанр")
            print("4. Удалить заказ")
            print("0. Выйти")

    @classmethod
    def some_input(cls, session: Session, menu_name: str, choose_input: str) -> str:

        try:
            choose = int(choose_input)
        except ValueError as e:
            print(e)
            choose = 0

        if menu_name == "Главное":
            if choose == 1:
                return "Добавить"
            if choose == 2:
                return "Прочитать"
            if choose == 3:
                return "Изменить"
            if choose == 4:
                return "Удалить"
            return "Exit"

        if menu_name == "Добавить":
            if choose == 1:
                create_human(session=session)
            if choose == 2:
                create_book(session=session)
            if choose == 3:
                create_genre(session=session)
            if choose == 4:
                create_order(session=session)
            return "Главное"

        if menu_name == "Прочитать":
            if choose == 1:
                read_humans(session=session)
            if choose == 2:
                read_books(session=session)
            if choose == 3:
                read_genres(session=session)
            if choose == 4:
                read_orders(session=session)
            return "Главное"

        if menu_name == "Изменить":
            if choose == 1:
                update_human(session=session)
            if choose == 2:
                update_book(session=session)
            if choose == 3:
                update_genre(session=session)
            if choose == 4:
                update_order(session=session)
            return "Главное"

        if menu_name == "Удалить":
            if choose == 1:
                delete_human(session=session)
            if choose == 2:
                delete_book(session=session)
            if choose == 3:
                delete_genre(session=session)
            if choose == 4:
                delete_order(session=session)
            return "Главное"
