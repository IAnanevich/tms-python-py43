# Создать таблицу продуктов.
# Атрибуты продукта: id, название, цена, количество, комментарий.
# Реализовать CRUD (создание, чтение, обновление по id, удаление по id) для продуктов.
# Создать пользовательский интерфейс.
import os
import sqlite3


class _SQLiteClient:

    SEP = "\\" if os.name == 'nt' else "/"

    def __init__(self, path: str) -> None:
        self.session = self.__connect_to_session(path)

    @staticmethod
    def __connect_to_session(path: str) -> sqlite3.Connection:
        try:
            return sqlite3.connect(database=path)
        except sqlite3.Error as error:
            print(error)

    def __execute_query(self, query: str) -> None:
        cursor = self.session.cursor()
        try:
            cursor.execute(query)
            self.session.commit()
        except sqlite3.Error as error:
            print(error)

    def __execute_read_query(self, query: str) -> list:
        cursor = self.session.cursor()
        try:
            cursor.execute(query)
            return cursor.fetchall()
        except sqlite3.Error as error:
            print(error)

    def _create(self, name: str, fields: dict) -> None:
        self.__execute_query(
            f"CREATE TABLE IF NOT EXISTS {name} ({','.join([f'{key} {value}' for key, value in fields.items()])})"
        )

    def _insert(self, name: str, items: dict) -> None:
        self.__execute_read_query(f"INSERT INTO {name} ({','.join(items.keys())}) VALUES ({','.join(items.values())})")

    def _select(self, name: str, fields: list | None = None) -> list:
        return self.__execute_read_query(f"SELECT {','.join(fields) if isinstance(fields, list) else '*'} FROM {name}")


class DataBase(_SQLiteClient):

    def __init__(self, name: str) -> None:
        super().__init__(f"{os.getcwd()}{super().SEP}{name}.sqlite")
        self.name = name

    def create_table(self, name: str, fields: dict) -> None:
        self._create(name, fields)

    def insert_to_table(self, name: str, items: list) -> None:
        for item in items:
            self._insert(name, item)

    def select_from_table(self, name: str, fields: list = None) -> list:
        return self._select(name, fields)


if __name__ == "__main__":
    myDB = DataBase("mybase")
    myDB.create_table(name="products", fields={
        "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
        "name": "VARCHAR(20) NOT NULL",
        "price": "FLOAT",
        "count": "FLOAT",
        "comment": "VARCHAR(250)"
    })
    myDB.insert_to_table(name="products", items=[
        {
            "name": "'prod'",
            "price": "500",
            "count": "5",
            "comment": "''"
        },
        {
            "name": "'prod2'",
            "price": "3000",
            "count": "103",
            "comment": "'it is comment'"
        }
    ])
    print(myDB.select_from_table(name="products"))
