# Создать таблицу продуктов.
# Атрибуты продукта: id, название, цена, количество, комментарий.
# Реализовать CRUD (создание, чтение, обновление по id, удаление по id) для продуктов.
# Создать пользовательский интерфейс.

import sqlite3
from typing import Any


# подключение к сессии
def connect_to_session(path: str) -> Any:
    """
    connect to session
    :param path: path to date base
    :return: connection or None
    """
    try:
        return sqlite3.connect(database=path)
    except sqlite3.Error as error:
        print(error)


class ProductsList:
    """
    class for work with base
    """

    def __init__(self, session: sqlite3.Connection) -> None:
        """
        initialization
        :param session: our connection
        """
        self.session = session

    def create(self, query: str) -> None:
        """
        do smth
        :param query: string with command
        :return: None
        """
        cursor = self.session.cursor()
        try:
            cursor.execute(query)
            self.session.commit()
        except sqlite3.Error as error:
            print(error)

    def read(self, table: str) -> Any:
        """
        read the base
        :param table: name of base
        :return: information list
        """
        cursor = self.session.cursor()
        try:
            cursor.execute(f"select * from {table}")
            print(type(cursor.fetchall()))
            return cursor.fetchall()
        except sqlite3.Error as error:
            print(error)

    def update(self, field_change: str, id_number: int) -> None:
        """
        update field by id number
        :param field_change: name of field
        :param id_number: id our item
        :return: none
        """
        cursor = self.session.cursor()
        new_tt = input(f"Enter new value for '{field_change}': ")
        try:
            cursor.execute(
                f"UPDATE Products SET {field_change}='{new_tt}' WHERE id={id_number}"
            )
            self.session.commit()
            # print("Base is update")
        except sqlite3.Error as error:
            print(error)

    def delete_item(self, id_number: int) -> None:
        """
        delete item from base by id
        :param id_number: id of item for delete
        :return: none
        """
        cursor = self.session.cursor()
        try:
            cursor.execute(f"DELETE FROM Products WHERE id={id_number}")
            self.session.commit()
        except sqlite3.Error as error:
            print(error)


product = ProductsList(session=connect_to_session(path="./sql_products.sqlite"))
# создание базы
# create_table = """CREATE TABLE IF NOT EXISTS Products
# (id INTEGER PRIMARY KEY AUTOINCREMENT,
# name VARCHAR(20),
# price INTEGER,
# quantity INTEGER,
# comment VARCHAR(60)
# )"""
# product.create(query=create_table)
#
# create_items = """INSERT INTO Products (name, price, quantity, comment)
# VALUES
# ("mazda", 10, 2, "red"),
# ("volkswagen", 20, 1, "black"),
# ("gilly", 15, 6, "silver and red"),
# ("opel", 12, 4, "white"),
# ("lamborghini", 100, 1, "orange")
#  """
# product.create(query=create_items)

while True:
    print("\n What do you want to do?")
    print(
        "1. Read base",
        "2. Update base item by ID",
        "3. Delete item by ID",
        "0. Exit",
        sep="\n",
    )
    action_s = input("Please enter operation: ")
    if action_s.isdigit():
        action = int(action_s)
        if not action:
            print("Goodbye!")
            break
        elif 0 < action < 4:
            if action == 1:
                print(*product.read(table="Products"), sep="\n")
            elif action == 2:
                id_for_change = input("Enter id for changing: ")
                print("Choice field for changing: ")
                print(
                    "1. name",
                    "2. price",
                    "3. quantity",
                    "4. comment",
                    "0. Exit",
                    sep="\n",
                )
                field_for_change = input("Enter field for changing: ")
                try:
                    match int(field_for_change):
                        case 0:
                            continue
                        case 1:
                            product.update(
                                field_change="name", id_number=int(id_for_change)
                            )
                        case 2:
                            product.update(
                                field_change="price", id_number=int(id_for_change)
                            )
                        case 3:
                            product.update(
                                field_change="quantity", id_number=int(id_for_change)
                            )
                        case 4:
                            product.update(
                                field_change="comment", id_number=int(id_for_change)
                            )
                        case _:
                            print("You needed to enter number 1 - 4, or 0 for Exit")
                except ValueError as err:
                    print(err)
            elif action == 3:
                id_for_delete = input("Enter id for delete: ")
                try:
                    product.delete_item(id_number=int(id_for_delete))
                except ValueError as err:
                    print(err)
        else:
            print("You need to enter number 1 - 5, or 0 for Exit, try again")
    else:
        print(
            "You need to enter integer NUMBER to choose operation not String, try again"
        )
