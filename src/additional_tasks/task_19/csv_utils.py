# 1. Написать функции по работе с csv файлами в файле csv_utils.py:
#  - Чтение.
#  - Запись.
#  - Добавление записи (по позиции, по-умолчанию в конец).
#  - Удаление записи(по позиции, по-умолчанию последнюю).
# 2. Импортировать эти функции в новый файл (task_19_1.py). С помощью функций:
#  - Создать файл с информацией о товарах (Имя товара, цена, количество, комментарий).
#  - Прочесть файл
#  - Добавить новую позицию в конец.
#  - Удалить третью строку.
# 3. Вернуться в файл csv_utils.py. Написать функции:
#  - Создать функцию подсчета полной суммы всех товаров.
#  - Создать функцию поиска самого дорогого товара.
#  - Создать функцию самого дешевого товара.
#  - Создать функцию уменьшения количества товара (на n, по-умолчанию на 1, n вводится с клавиатуры)
# Проверка работы функций осуществляется в task_19_2.py.
# Как итог у вас должно получится 3 файла (csv_utils.py, task_19_1.py, task_19_2.py), также один файл csv формата:
#  - csv_utils.py - содержит все функции для работы с csv файлом
#  - task_19_1.py - происходит работа с файлом и его содержимым используя функции из csv_utils.py
#  - task_19_2.py - происходит проверка работы функций из пункта в), используя новые функции из пункта

import csv


class CSVWork:
    """
    path to db class
    """

    def __init__(self, path_to_file: str):
        self.path_to_file = path_to_file

    def read_csv(self) -> None:
        """
        read content of csv file
        :return: None
        """
        with open(self.path_to_file) as file:
            print(file.read())

    def create_csv(self, data: list[list]) -> None:
        """
        create csv file with content 'data'
        :param data: information for writing to file
        :return: None
        """
        with open(self.path_to_file, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(data)

    def add_item_csv(
        self, note: list[str], place: int = 0
    ) -> None:  # по умолчанию 0 - тогда пишет в конец
        """
        add new SKU to table by orders number
        :param note: data for add
        :param place: position for insert data
        :return: None
        """
        # если хотим дописать внутрь таблицы
        if place:
            # считываем содержимое файла, чтобы потом его перезаписать в нужном порядке
            with open(self.path_to_file, "r") as file:
                csv_content = file.readlines()
            # записываем данные в файл
            with open(self.path_to_file, "w", newline="") as file:
                writer = csv.writer(file)
                # записываем в файл построчно
                for i in range(
                    len(csv_content) + 1
                ):  # количество строк с учетом 1 добавляемой
                    if i == place:
                        writer.writerow(note)
                    else:
                        # преобразовываем считанную строку в массив, подрезая символ "\n" в конце
                        writer.writerow(
                            csv_content[i if i < place else i - 1][:-1].split(sep=",")
                        )
        else:
            # если дописываем в конец файла
            with open(self.path_to_file, "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(note)

    def del_item_csv(self, place: int = 0) -> None:
        """
        delete SKU from table by orders number
        :param place: position for delete
        :return: None
        """
        # считываем содержимое файла, чтобы потом его перезаписать в нужном порядке
        with open(self.path_to_file, "r") as file:
            csv_content = file.readlines()
        # записываем данные в файл
        with open(self.path_to_file, "w", newline="") as file:
            writer = csv.writer(file)
            # записываем в файл построчно
            if place:
                for i in range(len(csv_content)):  # количество строк текущей таблицы
                    if i == place:
                        continue
                    else:
                        # преобразовываем считанную строку в массив, подрезая символ "\n" в конце
                        writer.writerow(csv_content[i][:-1].split(sep=","))
            # либо не пишем последнюю строку
            else:
                for j in range(len(csv_content) - 1):
                    writer.writerow(csv_content[j][:-1].split(sep=","))

    # - Создать функцию подсчета полной суммы всех товаров.
    def sum_all_item(self) -> None:
        """
        print cost of all skus
        :return: None
        """
        cost_all_item = 0.0
        # считываем содержимое как словарь
        with open(self.path_to_file, "r") as file:
            reader = csv.DictReader(file)
            # перебором находим сумму всех товаров
            for item in reader:
                cost_all_item += float(item["price"]) * int(item["quantity"])
        print("Cost of all items is:", cost_all_item)

    #  - Создать функцию поиска самого дорогого товара.
    def max_item_price(self) -> None:
        """
        find max cost and info about sku
        :return: None
        """
        max_price = 0.0
        # находим максимальную стоимость
        with open(self.path_to_file, "r") as file:
            reader = csv.DictReader(file)
            for item in reader:
                max_price = (
                    float(item["price"])
                    if float(item["price"]) > max_price
                    else max_price
                )
        # выводи информацию по товарам с максимальной стоимостью
        with open(self.path_to_file, "r") as file:
            reader = csv.DictReader(file)
            for item in reader:
                if float(item["price"]) == max_price:
                    print("Max price is:", max_price)
                    print("Info about this SKU:", item["sku"], item["quantity"])

    #  - Создать функцию самого дешевого товара.
    def min_item_price(self) -> None:
        """
        find mшт cost and info about sku
        :return: None
        """
        min_price = 1000000000000.0
        # находим минимальную стоимость
        with open(self.path_to_file, "r") as file:
            reader = csv.DictReader(file)
            for item in reader:
                min_price = (
                    float(item["price"])
                    if float(item["price"]) < min_price
                    else min_price
                )
        # выводи информацию по товарам с минимальной стоимостью
        with open(self.path_to_file, "r") as file:
            reader = csv.DictReader(file)
            for item in reader:
                if float(item["price"]) == min_price:
                    print("Min price is:", min_price)
                    print("Info about this SKU:", item["sku"], item["quantity"])

    #  - Создать функцию уменьшения количества товара (на n, по-умолчанию на 1, n вводится с клавиатуры)
    def change_item(self, item_id: int) -> None:
        """
        change quantity of sku by id
        :param item_id:
        :return:
        """
        # считываем содержимое файла, чтобы потом его перезаписать в нужном порядке
        with open(self.path_to_file, "r") as file:
            csv_content = file.readlines()
        # записываем данные в файл с изменением по количеству
        with open(self.path_to_file, "w", newline="") as file:
            writer = csv.writer(file)
            # с каждой строкой работаю как со списком
            for i in range(len(csv_content)):
                array_write = csv_content[i][:-1].split(sep=",")
                if i == item_id:
                    # с клавиатуры вводится количество для изменения, если введено не число - уменьшаем на 1
                    numb = input("Enter number for decrease quantity: ")
                    if numb.isdigit():
                        array_write[2] = str(int(array_write[2]) - int(numb))
                    else:
                        array_write[2] = str(int(array_write[2]) - 1)
                writer.writerow(array_write)
