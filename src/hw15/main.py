# https://pxstudio.pw/blog/15-besplatnyh-api-dlya-napisaniya-testovyh-prilozhenij
# Выбрать отсюда любую API и с помощью библиотеки requests отправить запрос.
# Посмотреть на данные в респонсе, сделать для них класс с полями (как в 13 дз связть с бд
# через sqlalchemt) и две функции, создание и чтение
# Сделать меню (1. Создать, 2. Прочитать, 0. Выйти)
# 1 -> Создаете запись в бд с данными с респонса
# 2 -> Читаете все данные из бд

# скрипт забирает по апи курс USD из беларусбанка и агропром. сохраняет в 1 таблицу
# для добавления нового банка нужно добавить класс в app/bank
# и добавить название банка в список bank_list (rate_manager.py)
# сделал фабрикой.

from app.rate_manager import RateManager
from helpers import print_list, print_color
from constant import MENU


rate = RateManager()


def menu():
    def sub_menu_1():  # заказы
        # Шлем по всем апи запросы. сохраняем в БД
        rate.update_list()

    def sub_menu_2():
        # показываем список USD всех банков
        items = rate.list()

        if items:
            print_list(items)
        else:
            print_color("Список курсов пуст", "red")

    while (ch := input(MENU["main"])) != "0":
        if ch == '1':
            sub_menu_1()
        elif ch == '2':
            sub_menu_2()


if __name__ == '__main__':
    menu()
