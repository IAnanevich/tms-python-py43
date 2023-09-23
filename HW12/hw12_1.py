# ДЗ 12
# Создать таблицу продуктов
# Атрибуты продукта: id, название, цена, количество, комментарий.
# Реализовать CRUD (создание+, чтение+, обновление по id, удаление по id) для продуктов.
# Создать пользовательский интерфейс.
import sqlite3


class Products:

    def __init__(self) -> None:
        self.session = sqlite3.connect(database="sql.sqlite")
        q = """
        CREATE TABLE IF NOT EXISTS Products
        (id INTEGER Primary Key Autoincrement,
            name VARCHAR(100) NOT NULL,
            price INTEGER NOT NULL,
            qty INTEGER NOT NULL,
            comments VARCHAR(100))
        """
        self.execute(query=q)

    def execute(self, query: str) -> bool:
        """
        Выполняет произвольный запрос
        :param query: текс запроса
        :return: выполнена ли операция успешно
        """
        cursor = self.session.cursor()
        try:
            cursor.execute(query)
            self.session.commit()
            return True
        except sqlite3.Error as e:
            print(e)
            return False

    def read(self) -> list:
        """
        Считывает все записи таблицы
        :return: список строк в таблице
        """
        cursor = self.session.cursor()
        try:
            cursor.execute("select * from Products")
            return list(cursor.fetchall())
        except sqlite3.Error as e:
            print(e)
            return []

    def add(self, name: str, price: float, qty: float, comments: str = "") -> bool:
        """
        Добовляет запись в таблицу
        :param name: Наименование
        :param price: Цена
        :param qty: Количество
        :param comments: Комменарий
        :return: выполнена ли операция успешно
        """
        q = f"INSERT INTO Products (name, price, qty, comments) VALUES ('{name}', {price}, {qty}, '{comments}')"
        cursor = self.session.cursor()
        try:
            cursor.execute(q)
            self.session.commit()
            return True
        except sqlite3.Error as e:
            print(e)
            return False

    def update(self, row_id: int, name: str, price: float, qty: float, comments: str = "") -> bool:
        # """
        # Обновляет запись в таблице
        # :param row_id: id записи
        # :param name: Наименование
        # :param price: Цена
        # :param qty: Количество
        # :param comments: Комменарий
        # :return: выполнена ли операция успешно
        # """
        q = f"""
        UPDATE Products
        SET name = '{name}', price = {price}, qty = {qty}, comments = '{comments}'
        WHERE id = {row_id}
        """
        cursor = self.session.cursor()
        try:
            cursor.execute(q)
            self.session.commit()
            return True
        except sqlite3.Error as e:
            print(e)
            return False

    def delete(self, row_id: int) -> bool:
        # """
        # Удаляет запись из таблицу
        # :param row_id: id записи
        # :return: выполнена ли операция успешно
        # """
        q = f"DELETE FROM Products WHERE ID = '{row_id}'"
        cursor = self.session.cursor()
        try:
            cursor.execute(q)
            self.session.commit()
            return True
        except sqlite3.Error as e:
            print(e)
            return False


p = Products()
p.add(name="HW12", price=10.22, qty=12, comments="DB SQL Lite")
p.add(name="HW12", price=10.22, qty=12, comments="DB SQL Lite")
print(p.read())  # [(1, 'HW12', 10.22, 12, 'DB SQL Lite'), (2, 'HW12', 10.22, 12, 'DB SQL Lite')]

p.delete(row_id=2)
print(p.read())  # [(1, 'HW12', 10.22, 12, 'DB SQL Lite')]

p.update(row_id=1, name="My homework 12", price=1000.01, qty=1.5, comments="I use DB SQL Lite")
print(p.read())  # [(1, 'My homework 12', 1000.01, 1.5, 'I use DB SQL Lite')]
