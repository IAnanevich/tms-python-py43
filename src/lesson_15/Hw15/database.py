# Выбрать любую API и с помощью библиотеки requests отправить запрос.
# Посмотреть на данные в response, сделать для них класс с полями (как в 13 дз связать с бд через sqlalchemy)
# и две функции, создание и чтение.
# Сделать меню (1. Создать, 2. Прочитать, 0. Выйти)
# 1 -> Создаете запись в бд с данными с response
# 2 -> Читаете все данные из бд

import requests
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
import json

engine = create_engine('sqlite:///random_users.db', echo=True)
Session = sessionmaker(bind=engine)
Base = declarative_base()
session = Session()


def get_url():
    url = 'https://randomuser.me/api/?inc=gender,name,email,registered,phone,id,location'
    data = requests.get(url).json()
    return data


result = get_url()

with open('result.json', 'w') as json_file:
    json.dump(result, json_file)

