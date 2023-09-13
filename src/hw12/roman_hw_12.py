'''Создать таблицу продуктов. Атрибуты продукта: id, название, цена, количество,
комментарий. Реализовать CRUD (создание, чтение, обновление по id, удаление по id)
для продуктов. Создать пользовательский интерфейс.'''
import sqlite3

# Подключение к базе данных
conn = sqlite3.connect('products.db')
c = conn.cursor()


# Создание таблицы продуктов
def create_table():
    c.execute('''CREATE TABLE IF NOT EXISTS products 
                 (id INTEGER PRIMARY KEY, 
                 name TEXT, 
                 price REAL, 
                 quantity INTEGER, 
                 comment TEXT)''')


# Добавление продукта
def add_product(id, name, price, quantity, comment):
    c.execute("INSERT OR REPLACE INTO products (id, name, price, quantity, comment) VALUES (?, ?, ?, ?, ?)",
              (id, name, price, quantity, comment))
    conn.commit()


# Получение всех продуктов
def get_all_products():
    c.execute("SELECT * FROM products")
    return c.fetchall()


# Обновление продукта по id
def update_product(id, new_values):
    for key, value in new_values.items():
        c.execute("UPDATE products SET {} = ? WHERE id = ?".format(key), (value, id))
    conn.commit()


# Удаление продукта по id
def delete_product(id):
    c.execute("DELETE FROM products WHERE id = ?", (id,))
    conn.commit()


# Создание таблицы
create_table()

# Пример использования

# Добавление новых продуктов
add_product(1, "Хлеб", 1.5, 10, "Свежий хлеб")
add_product(2, "Молоко", 2.0, 5, "Молоко 3.5%")
add_product(3, "Сырок", 0.8, 10, "Сырок ТОП")

# Получение всех продуктов
products = get_all_products()
for product in products:
    print(product)

# Обновление продуктов с id=1 и 2
update_product(1, {"price": 1.2, "quantity": 8, "comment": "Черствый хлеб"})
update_product(2, {"price": 1.5, "quantity": 2, "comment": "Скисшее молоко"})

# Удаление продукта с id=3
delete_product(3)

conn.close()
