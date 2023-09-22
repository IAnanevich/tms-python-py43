# https://pxstudio.pw/blog/15-besplatnyh-api-dlya-napisaniya-testovyh-prilozhenij
# Выбрать отсюда любую API и с помощью библиотеки requests отправить запрос.
# Посмотреть на данные в респонсе, сделать для них класс с полями (как в 13 дз связть с бд через sqlalchemt) и
# две функции, создание и чтение
# Сделать меню (1. Создать, 2. Прочитать, 0. Выйти)
# 1 -> Создаете запись в бд с данными с респонса
# 2 -> Читаете все данные из бд

import requests
from sqlalchemy.orm import session
from menu import Menu

url = 'https://ipinfo.io/161.185.160.93/geo'
result = requests.get(url)
print(result.json())
menu_1 = "Главное"

while True:
    Menu.menu_viz(menu=menu_1)
    menu_1 = Menu.menu_imp(session=session, menu=menu_1, choose=input(' '))
    if menu_1 == 'Выход':
        break
