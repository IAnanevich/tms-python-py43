# Создать словарь в качестве ключа которого будет 6 - ти начное число(id).
# В качестве значений кортеж состоящий из 2-х элементов - имя (str), возраст(int)
# Сделать около 5-6 элементов словаря. Записать данный словарь на диск в json-файл

import json

information = {
    123456: ('Ivan', 54),
    789012: ('Lena', 34),
    789011: ('Alex', 44),
    789056: ('Dana', 26),
    789018: ('Max', 41),
    789010: ('Lina', 40)
}

with open('katya_7_3.json', 'w') as new_file:
    new_file.write(json.dumps(information))

with open('katya_7_3.json', 'r') as new_file:
   print(json.loads(new_file.read()))
