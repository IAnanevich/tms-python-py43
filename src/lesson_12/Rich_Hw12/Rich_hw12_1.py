import sqlite3

# Создание и подключение к базе данных
conn = sqlite3.connect('products.db')
cursor = conn.cursor()

# Создание таблицы продуктов, если она не существует
cursor.execute('''CREATE TABLE IF NOT EXISTS products (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    price REAL,
                    quantity INTEGER,
                    comment TEXT
                )''')
conn.commit()


def create_product():
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    quantity = int(input("Enter product quantity: "))
    comment = input("Enter product comment: ")

    cursor.execute("INSERT INTO products (name, price, quantity, comment) VALUES (?, ?, ?, ?)",
                   (name, price, quantity, comment))
    conn.commit()
    print("Product created successfully.")


def read_products():
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    for product in products:
        print(
            f"ID: {product[0]}, Name: {product[1]}, Price: {product[2]}, Quantity: {product[3]}, Comment: {product[4]}")


def update_product():
    product_id = int(input("Enter product ID to update: "))
    name = input("Enter new product name: ")
    price = float(input("Enter new product price: "))
    quantity = int(input("Enter new product quantity: "))
    comment = input("Enter new product comment: ")

    cursor.execute("UPDATE products SET name=?, price=?, quantity=?, comment=? WHERE id=?",
                   (name, price, quantity, comment, product_id))
    conn.commit()
    print("Product updated successfully.")


def delete_product():
    product_id = int(input("Enter product ID to delete: "))
    cursor.execute("DELETE FROM products WHERE id=?", (product_id,))
    conn.commit()
    print("Product deleted successfully.")


while True:
    print("Options:")
    print("1. Create Product")
    print("2. Read Products")
    print("3. Update Product")
    print("4. Delete Product")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        create_product()
    elif choice == '2':
        read_products()
    elif choice == '3':
        update_product()
    elif choice == '4':
        delete_product()
    elif choice == '5':
        print("by!")
        break
    else:
        print("Invalid choice. Please try again.")
