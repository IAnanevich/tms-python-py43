# https://pxstudio.pw/blog/15-besplatnyh-api-dlya-napisaniya-testovyh-prilozhenij
# Выбрать любую API и с помощью библиотеки requests отправить запрос.
# Посмотреть на данные в response, сделать для них класс с полями (как в 13 дз связать с бд через sqlalchemy)
# и две функции, создание и чтение.
# Сделать меню (1. Создать, 2. Прочитать, 0. Выйти)
# 1 -> Создаете запись в бд с данными с response
# 2 -> Читаете все данные из бд


import requests
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

# создаем сессию для работы с БД
engine = create_engine("sqlite:///university_hw15.db", echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class University(Base):
    """
    class for information about universities
    """
    __tablename__ = "university"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(150), nullable=False)
    website = Column(String(100), nullable=False)
    country = Column(String(50), nullable=False)


Base.metadata.create_all(engine)


# обновление базы
def create_base() -> None:
    """
    complete base with information from the response from API
    :return: None
    """
    country_query = input("Please, enter country for search university: ")
    result = requests.get(
        f"http://universities.hipolabs.com/search?country={country_query}"
    )
    if result.status_code == 200:
        uni_data = result.json()
        for item in uni_data:
            print(item)
            uni_item = University(
                name=item["name"], website=item["web_pages"][0], country=item["country"]
            )
            session.add(uni_item)
        session.commit()
    else:
        print("Some error")


# считывание базы
def read_base() -> None:
    """
    read information from base
    :return: None
    """
    for item in session.query(University).all():
        print(item.id, item.name, item.website, item.country)


# основная программа
while True:
    print("*** What do you want to do with DB?")
    print("1. Create base", "2. Read base", "0. Exit", sep="\n")
    action_s = input("Please enter operation: ")
    if action_s.isdigit():
        action = int(action_s)
        if not action:
            print("Goodbye!")
            break
        if action == 1:
            create_base()
        elif action == 2:
            read_base()
        else:
            print("!!!You need to enter number 1 - 5, or 0 for Exit, try again")
    else:
        print(
            "!!!You need to enter integer NUMBER to choose operation not String, try again"
        )
