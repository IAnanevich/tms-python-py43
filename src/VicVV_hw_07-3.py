# Запись в файл json

import json

_dict = {}
_age = 10
for _id in range(123456, 123465):
    _age = _age + 3
    _dict[_id] = (f'Pers_{_age}', _age)
print(_dict)

with open("example.json", "w") as json_file:
    json.dump(_dict, json_file)
