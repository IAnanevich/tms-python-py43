# Создать словарь в качестве ключа которого будет 6-ти значное число (id), а в качестве значений кортеж
# состоящий из 2-х элементов - имя (str), возраст(int). Сделать около 5-6 элементов словаря.
# Записать данный словарь на диск в json-файл.
# ========================================================================================================
import json
from typing import Dict, Tuple, Any

def write_dict_to_json(filename: str, data: Dict[int, Tuple[str, int]]) -> None:
    """
    Write a dictionary to a JSON file.
    :param filename: The name of the JSON file to write.
    :param data:The dictionary to be written to the JSON file. The keys are 6-digit numbers (id),
                     and the values are tuples containing a name (str) and an age (int).
    :return: None
    """
    with open(filename, 'w') as file:
        json.dump(data, file)


def read_dict_from_json(filename: str) -> Dict[int, Tuple[str, int]]:
    """
    Read a dictionary from a JSON file.
    :param filename: The name of the JSON file to read.
    :return:The dictionary read from the JSON file. The keys are 6-digit numbers (id),
              and the values are tuples containing a name (str) and an age (int).
    """
    with open(filename, 'r') as file:
        loaded_data = json.load(file)
    return loaded_data

# Create dict

data = {
    123456: ("Ani", 21),
    234567: ("Sofu", 22),
    345678: ("Serg", 23),
    456789: ("Alex", 25),
    567890: ("Ivan", 33),
    678901: ("Eve", 48)
}

# Write dict to json

write_dict_to_json('data.json', data)

# Read dict from json
loaded_data = read_dict_from_json("data.json")
print(loaded_data)
