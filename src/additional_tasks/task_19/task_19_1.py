# 2. Импортировать эти функции в новый файл (task_19_1.py). С помощью функций:
# все функции прописала в классе
from csv_utils import CSVWork   # type: ignore

file_csv = CSVWork("test.csv")
data_to_create = [
    ["sku", "price", "quantity", "comment"],
    ["peach", "2.5", "15", "fresh"],
    ["banana", "1.58", "35", "for sale"],
    ["pineapple", "4.5", "6", "not bad"],
    ["orange", "3.2", "17", "not fresh"],
]

#  - Создать файл с информацией о товарах (Имя товара, цена, количество, комментарий).
file_csv.create_csv(data=data_to_create)

#  - Прочесть файл
file_csv.read_csv()

#  - Добавить новую позицию в конец.
sku_add_new = ["apple", "2.8", "32", "fresh"]
file_csv.add_item_csv(note=sku_add_new)
file_csv.read_csv()

#  - Удалить третью строку.
file_csv.del_item_csv(place=3)

# выводим результат
file_csv.read_csv()
