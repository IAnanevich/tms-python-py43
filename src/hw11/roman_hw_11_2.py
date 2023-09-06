# Сделать функцию для фильтрации емейла (регуляркой)
import re
from typing import Union


def filter_email(email: str) -> Union[str, None]:
    """
    Функция для фильтрации почтового адреса с использованием регулярного выражения.

    Аргументы:
    - email (str): Почтовый адрес для фильтрации.

    Возвращает:
    - Union[str, None]: Отфильтрованный почтовый адрес или None, если адрес не соответствует формату.
    """

    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        return email
    else:
        return None


email1 = 'example@example.com'
filtered_email1 = filter_email(email1)
if filtered_email1:
    print(f"Отфильтрованный почтовый адрес: {filtered_email1}")
else:
    print(f"Почтовый адрес {email1} не соответствует формату")

email2 = 'example.com'
filtered_email2 = filter_email(email2)
if filtered_email2:
    print(f"Отфильтрованный почтовый адрес: {filtered_email2}")
else:
    print(f"Почтовый адрес {email2} не соответствует формату")
