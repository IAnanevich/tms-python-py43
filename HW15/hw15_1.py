# https://pxstudio.pw/blog/15-besplatnyh-api-dlya-napisaniya-testovyh-prilozhenij
# Выбрать отсюда любую API и с помощью библиотеки requests отправить запрос.
# Посмотреть на данные в респонсе,
# сделать для них класс с полями (как в 13 дз связть с бд через sqlalchemt) и две функции, создание и чтение
# Сделать меню (1. Создать, 2. Прочитать, 0. Выйти)
# 1 -> Создаете запись в бд с данными с респонса
# 2 -> Читаете все данные из бд
from managers.rates import RatesManager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Menu:

    @classmethod
    def draw_menu(cls) -> None:

        # Главное
        print("1. Добавить")
        print("2. Прочитать")
        print("0. Выйти")

    @classmethod
    def some_input(cls, choose_input: str) -> str:

        # Приведем любой выбор к числу
        try:
            choose = int(choose_input)
        except ValueError as e:
            print(e)
            choose = 0

        # Главное меню
        if choose == 1:
            # "Добавить"
            RatesManager.add_rates(session=session)
            return "Добавить"
        if choose == 2:
            # "Прочитать"
            RatesManager.draw_rates(session=session)
            return "Прочитать"
        return "Exit"


engine = create_engine("sqlite:///dz13.db", echo=True)
Sessions = sessionmaker(bind=engine)
session = Sessions()

while True:
    Menu.draw_menu()
    if "Exit" == Menu.some_input(choose_input=input(">>>")):
        break
