import sqlite3


def connect_to_sql(path: str) -> sqlite3.Connection | None:
    """
    connect to sql
    :param path:
    :return: connection | None
    """
    try:
        return sqlite3.connect(database=path)
    except sqlite3.Error as error:
        print(error)


class Produce:
    """
    for working with databases
    """

    def __init__(self, session: sqlite3.Connection) -> None:
        """
        initializer
        :param session: connection
        """
        self.session = session

    def create(self, query: str) -> None:
        """
        creation of a database
        :param query: string with commands
        :return: None
        """
        cursor = self.session.cursor()
        try:
            cursor.execute(query)
            self.session.commit()
        except sqlite3.Error as error:
            print(error)

    def read(self) -> list:
        """
        reading the database
        :return:  in list format
        """
        cursor = self.session.cursor()
        try:
            cursor.execute(f"SELECT * FROM SQLite3Produce")
            return list(cursor.fetchall())
        except sqlite3.Error as error:
            print(error)
            return []

    def update(self, change: str, id_produce: int) -> None:
        """
        changing element by id
        :param change: new value
        :param id_produce: id produce
        :return: None
        """
        cursor = self.session.cursor()
        try:
            cursor.execute(f"UPDATE SQLite3Produce SET {change} WHERE {id_produce}")
            self.session.commit()
        except sqlite3.Error as error:
            print(error)

    def delete(self, id_produce: int) -> None:
        """
        removing element by id
        :param id_produce: id-produce
        :return: None
        """
        cursor = self.session.cursor()
        try:
            cursor.execute(f"DELETE SQLite3Produce WHERE {id_produce}")
            self.session.commit()
        except sqlite3.Error as e:
            print(e)


produce_1 = Produce(session=connect_to_sql(path="./produce.sqlite"))

create_table_produce = """
CREATE TABLE IF NOT EXISTS product (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(20) NOT NULL,
    cost INTEGER,
    quantity INTEGER,
    comment VARCHAR(20)
)
"""
produce_1.create(query=create_table_produce)

create_produce = """
INSERT INTO 
    users (id, name, cost, quantity, comment)
VALUES 
    ('milk', 1, 20,' ')
"""
produce_1.create(query=create_produce)
