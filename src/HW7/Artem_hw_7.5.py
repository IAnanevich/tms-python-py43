import json
import openpyxl
import csv

wb = openpyxl.load_workbook('test.xlsx')
print(wb)

with open('lines.json', 'r') as file_j:
    data = json.load(file_j)
    with open('test.xlsx', 'w') as file_x:
        writer = csv.writer(file_x)
        writer.writerows(
            (
                data
            )
        )
