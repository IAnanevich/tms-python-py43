import sqlite3


def connect_to_session(path: str) -> sqlite3.Connection:
    """
        connecting from a session
        :param path: file path
        :return:
        """
    try:
        return sqlite3.connect(database=path)
    except sqlite3.Error as error:
        print(error)


class FoodStuff:
    def __init__(self, session: sqlite3.Connection) -> None:
        """

        :param session: connecting from a session
        """
        self.session = session

    def create(self, query: str) -> None:
        """
        creating a table
        :param query: any data
        :return:
        """
        cursor = self.session.cursor()
        try:
            cursor.execute(query)
            self.session.commit()

        except sqlite3.Error as error:
            print('create: ', error)

    def read(self, table: str):
        """
        reading the table
        :param table: reading the created table using the method "create"
        :return:
        """
        cursor = self.session.cursor()
        try:
            cursor.execute(f'select * from {table}')
            return cursor.fetchall()
        except sqlite3.Error as error:
            print('read: ', error)

    def update(self, id_field: int, any_field: str):
        """
        updating table values
        :param id_field: column id
        :param any_field: values a new field
        :return:
        """
        cursor = self.session.cursor()
        any_field = input(f'update field on: ')
        try:
            cursor.execute(f'UPDATE products SET field = {any_field} WHERE id_field = {id_field}')
            return cursor.fetchall()
        except sqlite3.Error as error:
            print('update: ', error)

    def delete(self, id_field: int) -> None:
        """
        method for deleting a field by id
        :param id_field: column id
        :return:
        """
        cursor = self.session.cursor()
        try:
            cursor.execute(f'DELETE FROM products WHERE id_field = {id_field}')
        except sqlite3.Error as error:
            print('delete: ', error)

    def insert(self, id_insert: int, title: str, price: float, amount: float, comment: str) -> None:
        """
        method for adding a row to the database
        :param id_insert:
        :param title:
        :param price:
        :param amount:
        :param comment:
        :return:
        """
        cursor = self.session.cursor()
        try:
            cursor.execute(f"INSERT INTO products VALUES (?, ?, ?, ?, ?);",
                           (id_insert, title, price, amount, comment))
        except sqlite3.Error as error:
            print('insert', error)


products = FoodStuff(session=connect_to_session(path='./foodstuff.sqlite'))
create_table_products = """
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(20) NOT NULL,
    price FLOAT,
    amount FLOAT,
    comment VARCHAR(100)
)
"""
products.create(query=create_table_products)

# add_products = """
# INSERT INTO
#     products(title, price, amount, comment)
# VALUES
#     ('meet', 11.34, 34, 'pork'),
#     ('milk', 3.20, 100, 'cows milk'),
#     ('bred', 1.84, 56, 'millet'),
#     ('water', 0.98, 1000, 'still'),
#     ('eggs', 2.90, 10, 'c-3')
# """
# products.create(query=add_products)
# print(products.read(table='products'))

while True:
    print('1.Read table')
    print('2.Update field')
    print('3.Delete field')
    print('4.Add new field')
    print('5.Exit')

    choice = input('Выберете действие: ')
    if choice.isdigit():
        choice = int(choice)

        if choice == 1:
            print(products.read(table='products'))
        elif choice == 2:
            another_id = input('select the id field: ')
            print('1.title')
            print('2.price')
            print('3.amount')
            print('4.comment')
            another_field = input('choose the field to change it: ')
            if another_id.isdigit():
                if another_field == 1:
                    products.update(id_field=int(another_id), any_field='title')
                elif another_field == 2:
                    products.update(id_field=int(another_id), any_field='price')
                elif another_field == 3:
                    products.update(id_field=int(another_id), any_field='amount')
                elif another_field == 4:
                    products.update(id_field=int(another_id), any_field='comment')
                else:
                    print('choose an id from 1 to 5: ')
                    # print('problem in IF ELIF UPDATE')
        elif choice == 3:
            delete_id = int(input('delete id 1-5: '))
            products.delete(id_field=delete_id)
        elif choice == 4:
            products.insert(
                id_insert=int(input('id: ')),
                title=str(input('title: ')),
                price=float(input('price: ')),
                amount=float(input('amount: ')),
                comment=str(input('comment: '))
            )
        elif choice == 5:
            print('Successful exit')
            break
        else:
            print('Enter a number 1-5: ')
