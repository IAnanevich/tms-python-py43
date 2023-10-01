# Сделать меню через цикл while с выбором:
from sqlalchemy.orm import Session

from HW13.update_file import update_user, update_book, update_genre
from create_file import create_order, create_user, create_book, create_genre
from read_file import read_users, read_books, read_genres, read_orders
from delete_file import delete_user, delete_book, delete_order


class Menu:
    @classmethod
    def main_menu(cls, session: Session) -> int:
        while True:
            print("What do you want to do?")
            print(
                "1. Make an order",
                "2. Add data",
                "3. Read info from base",
                "4. Make changes to base",
                "5. Delete some information from base",
                "0. Exit",
                sep="\n",
            )
            action_s = input("Please enter operation: ")
            if action_s.isdigit():
                action = int(action_s)
                if 0 <= action < 6:
                    if action == 1:
                        Menu.make_order_menu(session=session)
                    elif action == 2:
                        Menu.add_menu(session=session)
                    elif action == 3:
                        Menu.read_menu(session=session)
                    elif action == 4:
                        Menu.make_changes_menu(session=session)
                    elif action == 5:
                        Menu.delete_menu(session=session)
                    return action
                else:
                    print("You need to enter number 1 - 5, or 0 for Exit, try again")
            else:
                print(
                    "You need to enter integer NUMBER to choose operation not String, try again"
                )

    # 1. Сделать заказ
    # Далее
    # 1 -> вы создаете запись в таблице заказ,
    # делаете апдейт баланса у человека уменьшаете на стоимость книги, уменьшаете кол-во книг -1
    #

    @classmethod
    def make_order_menu(cls, session: Session):
        create_order(session)

    # 2. Добавить
    # # 2 -> открывается другое меню:
    # # 1. Добавить юзера (создаете юзера)
    # # 2. Добавить книгу (создаете книгу)
    # # 3. Добавить жанр (создаете жанр)
    # # 0. Вернуться назад
    # # Пользователь вводит с клавиатуры все данные и вы создаете книгу, юзера или жанр в зависимости от выбора
    @classmethod
    def add_menu(cls, session: Session):
        print("What do you want to add?")
        print("1. Add user", "2. Add book", "3. Add genre", "0. Exit", sep="\n")
        try:
            add_numb = int(input("Choose number: "))
        except ValueError as error:
            print(error)
        else:
            if add_numb == 1:
                create_user(session)
            if add_numb == 2:
                create_book(session)
            if add_numb == 3:
                create_genre(session)

    # 3. Прочитать
    # # 3 -> открывается другое меню:
    # # 1. Посмотреть юзеров
    # # 2. Посмотреть книги
    # # 3. Посмотреть заказы
    # # 4. Посмотреть жанры
    # # 0. Вернуться назад
    @classmethod
    def read_menu(cls, session: Session):
        print("What do you want to read?")
        print(
            "1. Read users",
            "2. Read books",
            "3. Read orders",
            "4. Read genres",
            "0. Exit",
            sep="\n",
        )
        try:
            read_numb = int(input("Choose number: "))
        except ValueError as error:
            print(error)
        else:
            if read_numb == 1:
                read_users(session)
            if read_numb == 2:
                read_books(session)
            if read_numb == 3:
                read_orders(session)
            if read_numb == 4:
                read_genres(session)

    # 4. Изменить

    # 4 -> открывается другое меню:
    # 1. Изменить юзера
    # 2. Изменить книгу
    # 3. Изменить жанр
    # 0. Вернуться назад
    #
    @classmethod  # изменить!
    def make_changes_menu(cls, session: Session):
        print("What do you want to update?")
        print(
            "1. Update user", "2. Update book", "3. Update genre", "0. Exit", sep="\n"
        )
        try:
            update_numb = int(input("Choose number: "))
        except ValueError as error:
            print(error)
        else:
            if update_numb == 1:
                update_user(session)
            if update_numb == 2:
                update_book(session)
            if update_numb == 3:
                update_genre(session)

    # 5. Удалить
    # 5 -> открывается другое меню:
    # 1. Удалить юзера
    # 2. Удалить книгу
    # 3. Удалить жанр
    # 0. Вернуться назад
    #
    # удаляет выбранную сущность по id который запрашиваете у пользователя
    @classmethod
    def delete_menu(cls, session: Session):
        print("What do you want to delete?")
        print(
            "1. Delete user", "2. Delete book", "3. Delete genre", "0. Exit", sep="\n"
        )
        try:
            delete_numb = int(input("Choose number: "))
        except ValueError as error:
            print(error)
        else:
            if delete_numb == 1:
                delete_user(session)
            if delete_numb == 2:
                delete_book(session)
            if delete_numb == 3:
                delete_order(session)
