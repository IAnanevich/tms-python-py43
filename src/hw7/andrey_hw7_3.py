# Создать словарь в качестве ключа которого будет 6 -ти значное число (id),
# а в качестве значений кортеж состоящий из 2-х элементов - имя(str),
# Возраст(int). Сделать около 5-6 элементов словаря. Записать данный словарь на диск в json-файл.
import json

if __name__ == "__main__":
    var = {123456: ('Вася', 12),
           222222: ('Петя', 20),
           323524: ('Катя', 24),
           222364: ('Вика', 55),
           253564: ('Вика', 24),
           134364: ('Кира', 33)}

    with open('example.json', 'w') as file_json:
        json.dump(var, file_json)
