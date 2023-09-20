# https://pxstudio.pw/blog/15-besplatnyh-api-dlya-napisaniya-testovyh-prilozhenij
# Выбрать отсюда любую API и с помощью библиотеки requests отправить запрос.
# Посмотреть на данные в респонсе, сделать для них класс с полями (как в 13 дз связть с бд через sqlalchemt) и
# две функции, создание и чтение
# Сделать меню (1. Создать, 2. Прочитать, 0. Выйти)
# 1 -> Создаете запись в бд с данными с респонса
# 2 -> Читаете все данные из бд

import requests
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 1. Создаем подключение к базе данных
DATABASE_URL = "sqlite:///user_data.db"  # Используем SQLite как пример
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
Base = declarative_base()

# 2. Определяем класс для таблицы в базе данных
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    username = Column(String)
    email = Column(String, unique=True, index=True)

# 3. Создаем таблицу в базе данных (если она еще не создана)
Base.metadata.create_all(bind=engine)

# 4. Функция для отправки запроса к API и создания записей в базе данных
def create_users_from_api():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    if response.status_code == 200:
        users_data = response.json()
        session = Session()
        for user_data in users_data:
            user = User(
                name=user_data["name"],
                username=user_data["username"],
                email=user_data["email"]
            )
            session.add(user)
        session.commit()
        session.close()
        print("Записи успешно созданы в базе данных.")
    else:
        print("Ошибка при получении данных с API.")

# 5. Функция для чтения всех записей из базы данных
def read_all_users():
    session = Session()
    users = session.query(User).all()
    session.close()
    if users:
        for user in users:
            print(f"ID: {user.id}, Name: {user.name}, Username: {user.username}, Email: {user.email}")
    else:
        print("В базе данных нет записей о пользователях.")

# 6. Основное меню
while True:
    print("\nМеню:")
    print("1. Создать записи в базе данных из API")
    print("2. Прочитать все записи из базы данных")
    print("0. Выйти")
    choice = input("Выберите действие: ")

    if choice == "1":
        create_users_from_api()
    elif choice == "2":
        read_all_users()
    elif choice == "0":
        break
    else:
        print("Неверный выбор. Попробуйте снова.")
