# 3. Вернуться в файл csv_utils.py. Написать функции:

from csv_utils import CSVWork  # type: ignore

file_csv = CSVWork("test.csv")

file_csv.read_csv()

#  - Создать функцию подсчета полной суммы всех товаров.
file_csv.sum_all_item()

#  - Создать функцию поиска самого дорогого товара.
file_csv.max_item_price()

#  - Создать функцию самого дешевого товара.
file_csv.min_item_price()

#  - Создать функцию уменьшения количества товара (на n, по-умолчанию на 1, n вводится с клавиатуры)
file_csv.change_item(item_id=3)

# выводим результат
file_csv.read_csv()
