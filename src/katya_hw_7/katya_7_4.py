import csv
import json

with open('katya_7_3.json', 'r') as new_file:
    file_katya = json.loads(new_file.read())

with open('katya_7_4.csv', 'w') as new_file:
    writer = csv.writer(file_katya)