from sqlalchemy.orm import Session
from CreateMixin import create_user, create_book, create_order, create_genre
from ReadMixin import read_user, read_book, read_order, read_genre
from DeleteMixin import delete_user, delete_book, delete_order, delete_genre
from UpdateMixin import update_user, update_book, update_genre, update_order


class Menu:
    def menu_viz(cls, menu: str) -> None:
        """

        :param menu:
        :return:
        """
        if menu == 'Главное':
            print('1. Прочитать')
            print('2. Добавить')
            print('3. Изменить')
            print('4. Удалить')
            print('0. Выйти')

        if menu == 'Прочитать':
            print('1. Посмотреть пользователя')
            print('2. Посмотреть книги')
            print('3. Посмотреть заказы')
            print('4. Посмотреть жанры')
            print('0. Выйти')

        if menu == 'Добавить':
            print('1. Добавить пользователя')
            print('2. Добавить книгу')
            print('3. Добавить заказ')
            print('4. Добавить жанр')
            print('0. Выйти')

        if menu == 'Изменить':
            print('1. Изменить пользователя')
            print('2. Изменить книгу')
            print('3. Изменить заказ')
            print('4. Изменить жанр')
            print('0. Выйти')

        if menu == 'Удалить':
            print('1. Удалить пользователя')
            print('2. Удалить книгу')
            print('3. Удалить заказ')
            print('4. Удалить жанр')
            print('0. Выйти')

    def menu_imp(cls, session: Session, menu: str, choose: str):
        """

        :param session:
        :param menu:
        :param choose:
        :return:
        """
        try:
            choose = int(choose)
        except ValueError as error:
            print(error)
            choose = 0

        if menu == 'Главное':
            if choose == 1:
                return 'Прочитать'
            if choose == 2:
                return 'Добавить'
            if choose == 3:
                return 'Изменить'
            if choose == 4:
                return 'Удалить'
            return 'Выход'

        if menu == "Прочитать":
            if choose == 1:
                read_user(session=session)
            if choose == 2:
                read_book(session=session)
            if choose == 3:
                read_order(session=session)
            if choose == 4:
                read_genre(session=session)
            return "Главное"

        if menu == 'Добавить':
            if choose == 1:
                create_user(session=session)
            if choose == 2:
                create_book(session=session)
            if choose == 3:
                create_order(session=session)
            if choose == 4:
                create_genre(session=session)
            return "Главное"

        if menu == "Изменить":
            if choose == 1:
                update_user(session=session)
            if choose == 2:
                update_book(session=session)
            if choose == 3:
                update_order(session=session)
            if choose == 4:
                update_genre(session=session)
            return "Главное"

        if menu == "Удалить":
            if choose == 1:
                delete_user(session=session)
            if choose == 2:
                delete_book(session=session)
            if choose == 3:
                delete_order(session=session)
            if choose == 4:
                delete_genre(session=session)
            return "Главное"
