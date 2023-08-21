# Создать словарь в качестве ключа которого будет 6-ти значное число (id),
# а в качестве значений кортеж состоящий из 2-х элементов имя(str) возраст (int).
# Сделать около 5-6 элементов словаря. Записать данный словарь на диск в json-файл
import json

dict: dict[int, tuple[str, int]] = {
    123456: ('sergei', 5),
    654321: ('Aleksei', 15),
    987654: ('Aleksandr', 12),
    456789: ('Masha', 15),
}
filename = "people.json"
with open(filename, "w") as json_file:
    json.dump(dict, json_file)
print(f'Словарь записан в JSON-файл: {filename}')
