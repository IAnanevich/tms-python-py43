# Создать таблицу продуктов.
# Атрибуты продукта: id, название, цена, количество, комментарий.
# Реализовать CRUD (создание, чтение, обновление по id, удаление по id) для продуктов.
# Создать пользовательский интерфейс.

import sqlite3

# Create BD and connected

conn = sqlite3.connect("product.db")
cursor = conn.cursor()

# Create table products
cursor.execute(''' CREATE TABLE IF NOT EXISTS product (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT NOT NULL,
                   price REAL NOT NULL, 
                   quantity INTEGER NOT NULL,
                   comment TEXT)''')

# saving changes in DB
conn.commit()


# ----------------------------- CRUD -----------------------------------------------------------------------


# Create product
def create_product(name, price, quantity, comment):
    conn = sqlite3.connect('product.db')
    cursor = conn.cursor()

    cursor.execute(''' INSERT INTO product (name, price, quantity, comment)
                       VALUES (?, ?, ?, ?)''', (name, price, quantity, comment))


conn.commit()
conn.close()

# Read product
def read_product(product_id):
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM products WHERE id = ?', (product_id,))
    product = cursor.fetchone()

    conn.close()
    return product

# Update product

def update_product(product_id, name, price, quantity, comment):
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    cursor.execute('''UPDATE products
                      SET name = ?, price = ?, quantity = ?, comment = ?
                      WHERE id = ?''', (name, price, quantity, comment, product_id))

    conn.commit()
    conn.close()

# Delete product

def delete_product(product_id):
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    cursor.execute('DELETE FROM products WHERE id = ?', (product_id,))

    conn.commit()
    conn.close()

# Create user Interface

while True:
    print("\nМеню:")
    print("1. Добавить продукт")
    print("2. Просмотреть продукт")
    print("3. Обновить продукт")
    print("4. Удалить продукт")
    print("5. Выйти")

    choice = input("Выберите действие: ")

    if choice == '1':
        name = input("Введите название продукта: ")
        price = float(input("Введите цену продукта: "))
        quantity = int(input("Введите количество продукта: "))
        comment = input("Введите комментарий к продукту (опционально): ")
        create_product(name, price, quantity, comment)
        print("Продукт добавлен.")
    elif choice == '2':
        product_id = int(input("Введите id продукта для просмотра: "))
        product = read_product(product_id)
        if product:
            print("Информация о продукте:")
            print(f"ID: {product[0]}")
            print(f"Название: {product[1]}")
            print(f"Цена: {product[2]}")
            print(f"Количество: {product[3]}")
            print(f"Комментарий: {product[4]}")
        else:
            print("Продукт с указанным ID не найден.")
    elif choice == '3':
        product_id = int(input("Введите id продукта для обновления: "))
        name = input("Введите новое название продукта: ")
        price = float(input("Введите новую цену продукта: "))
        quantity = int(input("Введите новое количество продукта: "))
        comment = input("Введите новый комментарий к продукту (опционально): ")
        update_product(product_id, name, price, quantity, comment)
        print("Продукт обновлен.")
    elif choice == '4':
        product_id = int(input("Введите id продукта для удаления: "))
        delete_product(product_id)
        print("Продукт удален.")
    elif choice == '5':
        break
    else:
        print("Неверный выбор. Пожалуйста, выберите действие из меню.")
