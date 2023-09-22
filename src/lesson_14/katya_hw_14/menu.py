from sqlalchemy.orm import Session
from CreatMixin import create_ip_info
from ReadMixin import read_ip_info


class Menu:
    def menu_viz(menu: str) -> None:
        """
        :param menu:
        :return:
        """
        if menu == 'Главное':
            print('1. Создать')
            print('2. Читать')
            print('0. Выйти')

        if menu == 'Создать':
            print('1. Создать')
            print('0. Выйти')

        if menu == 'Прочитать':
            print('1. Читать')
            print('0. Выйти')

    def menu_imp(menu: str, choose: str):
        """
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
                return 'Создать'
            if choose == 2:
                return 'Читать'
            return 'Выход'

        if menu == "Прочитать":
            if choose == 1:
                read_ip_info()
            return "Главное"

        if menu == 'Создать':
            if choose == 1:
                create_ip_info()
            return "Главное"

