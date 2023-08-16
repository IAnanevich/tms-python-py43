# Прочитать сохраненный json-файл и записать данные на диск в csv-файл, первой строкой, которого
# озоглавив каждый столбец и добавив новый стоблец "телефон".
# ==========================================================================================================

import json
import csv
from typing import Dict, Tuple

def read_dict_from_json(filename: str) -> Dict[int, Tuple[str, int]]:
    """
    Read a dictionary from a JSON file.
    :param filename: The name of the JSON file.
    :return: A dictionary loaded from the JSON file.
    """
    with open(filename, 'r') as file:
        loaded_data = json.load(file)
    return loaded_data

def write_dict_to_csv(filename: str, data: Dict[int, Tuple[str, int]]) -> None:
    """
     Write a dictionary to a CSV file.
    :param filename: The name of the CSV file.
    :param data: The dictionary to write to the CSV file.
    """
    with open(filename, 'w', newline='') as file:
        csv_writer = csv.writer(file)

        # Write header row
        header = ["ID", "Name", "Age", "Phone"]
        csv_writer.writerow(header)

        # Write data rows
        for id, (name, age) in data.items():
            csv_writer.writerow([id, name, age, ""])  # Empty phone column for now


# Read dictionary from JSON file
loaded_data = read_dict_from_json("data.json")

# Write dictionary to CSV file
write_dict_to_csv("data.csv", loaded_data)
