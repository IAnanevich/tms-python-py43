"""
Создать таблицу продуктов.
Атрибуты продукта: id, название, цена, количество, комментарий.
Реализовать CRUD (создание, чтение, обновление по id, удаление по id)
для продуктов. Создать пользовательский интерфейс.
"""
import sqlite3


def con(path: str) -> sqlite3.Connection:
    """
    Establishes a connection to a SQLite database
    :param path: path
    :return: connection
    """
    try:
        return sqlite3.connect(database=path)
    except sqlite3.Error as error:
        print(error)


class Client:
    """
    Class for working with SQLite database
    Methods: __init__, ex_query
    Attributes: session
    """
    def __init__(self, session: sqlite3.Connection) -> None:
        """
        Initializes a new instance of the class
        :param session: session
        :return: None
        """
        self.session = session

    def ex_query(self, query: str, par=None) -> None:
        """
        Executes an SQL query
        :param query: str
        :param par: par
        :return: None
        """
        cursor = self.session.cursor()
        try:
            if par is None:
                cursor.execute(query)
            else:
                cursor.execute(query, par)
            self.session.commit()
        except sqlite3.Error as er:
            print(er)


client_1 = Client(session=con(path='C:\\Users\\user\\Desktop\\py\\tms-python-py43\\src\\h12\\sql.sqlite'))
print('[1]CREATE')
print('[2]READ')
print('[3]UPDATE')
print('[4]DELETE')
try:
    choice = int(input('Enter your choice: '))
    if choice == 1:
        q = """
        CREATE TABLE IF NOT EXISTS products(
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            name VARCHAR(20) NOT NULL,
            price FLOAT,
            quantity INTEGER,
            comment VARCHAR(100)
        )
        """
        client_1.ex_query(q)
        # почему AUTOINCREMENT не работает без PRIMARY KEY?
    elif choice == 2:
        q = """
        SELECT * FROM products
        """
        client_1.ex_query(q)
    elif choice == 3:
        try:
            print('What price do you want to change to for id?')
            c_price = float(input('Enter your choice: '))
            print('What id do you want to change for?')
            c_id = float(input('Enter your choice: '))
            q = """
            UPDATE products
            SET price = ?
            WHERE id = ?
            """
            client_1.ex_query(q, (c_price, c_id))
        except Exception as e:
            print(e)
    elif choice == 4:
        try:
            print('What id do you want to delete?')
            c_id = float(input('Enter your choice: '))
            q = """
            DELETE FROM products
            WHERE id = ?
            """
            client_1.ex_query(q, (c_id, ))
        except Exception as e:
            print(e)
    else:
        print('Try again')
except Exception as e:
    print(e)
