"""3. Создать словарь в качестве ключа которого будет 6-ти значное число (id),
а в качестве значений кортеж состоящий из 2-х элементов - имя(str), возраст(int).
Сделать около 5-6 элементов словаря. Записать данный словарь на диск в json-файл."""
import json

dict_ = {
        123456: ('Dhjm', 25),
        654321: ('Jy', 65),
        987456: ('Wewm', 87),
        745896: ('Pthy', 41),
        963852: ('Qertgh', 23)
}
with open('nastya_hw7_3.json', 'w') as f:
    json.dump(dict_, f)
