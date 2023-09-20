import sys
from models.product import Product
from faker import Faker
sys.path.insert(0, '/tms/hw12/tms-python-py43/src/hw12/')


def print_main_menu() -> None:
    print_color("""
           ******************************************************
           *         Выберите пункт меню                        *
           *         1. Прочитать запись                        *
           *         2. Создать запись со случайными данными    *
           *         3. Обновить запись                         *
           *         4. Удалить запись                          *       
           *         5. Выход                                   *
           ******************************************************""", "blue")


def print_color(text: str, color: str) -> None:
    access_color = {
        "green": "\033[32m",
        "blue": "\033[34m",
        "red": "\033[31m",
    }
    if color in access_color:
        print(f"{access_color[color]}{text}\033[34m")
    else:
        print(text)


product = Product()
# product.create()  # создаем таблицу
fake = Faker("ru_RU")  # объект для случайных записей
print_main_menu()  # рисуем меню
# flake8: noqa: C901
while True:
    menu = input('Выберете действие: ')
    if menu.isdigit():
        menu = int(menu)
        if menu == 1:
            _id = input('Введите ID записи: ')
            if _id.isdigit():
                filter = {
                    "id": int(_id),
                }
                result = product.get_list(filter=filter)
                if len(result):
                    print(result[0])
                else:
                    print_main_menu()
                    print(f"Данные по ID = {_id} не найдены")
            else:
                pass
        elif menu == 2:
            params = {
                "name": fake.name(),
                "price": fake.pyfloat(6, 2, True),
                "quantity": fake.pyint(2),
                "comment": fake.text(),
            }
            _id = product.insert(params=params)
            if _id > 0:
                print_main_menu()
                print_color(f"Добавлена запись с ID = {_id}", "green")
        elif menu == 3:
            _id = input('Введите ID записи для обновления случайными данными: ')
            params = {
                "name": fake.name(),
                "price": fake.pyfloat(6, 2, True),
                "quantity": fake.pyint(2),
                "comment": fake.text(),
            }
            if _id.isdigit():
                # TODO создаем заново объект т.к. хотим точно знать обновилось или нет. total_changes считает все
                #  изменения в сессии. а нам надо только в этой операции.
                product = Product()
                if product.update(id=int(_id), params=params):
                    print_color(f"Запись {_id} обновлена", "green")
                else:
                    print_color(f"Запись {_id} обновить не удалось", "red")
            else:
                print_main_menu()
                print_color("Ожидали числовое значение ID. Попробуйте еще раз", "red")
        elif menu == 4:
            _id = input('Введите ID записи для удаления: ')
            print_main_menu()
            if _id.isdigit():
                # TODO создаем заново объект т.к. хотим точно знать удалилась запись или нет. наверно есть более
                #  нормальный способ. пока так
                product = Product()
                if product.delete(id=int(_id)):
                    print_color(f"Запись {_id} удалена", "green")
                else:
                    print_color(f"Запись {_id} удалить не удалось", "red")
            else:
                print_color("Ожидали ID записи. Попробуйте еще раз", "red")
        elif menu == 5:
            print("Bye! 😎😎😎")
            break
        else:
            print_color("Выберите пункт 1-5", "red")
    else:
        print_color("Выберите пункт 1-5", "red")
