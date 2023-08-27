# Создать матрицу случайных чисел и сохранить ее в json файл.
# После прочесть ее, обнулить все четные элементы и сохранить в другой файл.
import json
from random import randint


def make_matrix(row: int, column: int) -> list[list[int]]:
    """
    create matrix row*column with random integer numbers from [1;100]
    :param row: number of rows
    :param column: number of columns
    :return: new matrix
    """
    my_matrix = []
    for _ in range(row):
        matrix_row = []
        for _ in range(column):
            matrix_row.append(randint(1, 100))
        my_matrix.append(matrix_row)
    return my_matrix


def change_even_value(matrix_for_change: list[list[int]]) -> list[list[int]]:
    """
    change matrix: replace even number in matrix by 0
    :param matrix_for_change: original matrix
    :return: changed matrix
    """
    for row_number in matrix_for_change:
        for i in range(len(row_number)):
            if not row_number[i] % 2:
                row_number[i] = 0
    return matrix_for_change


# задаем размерность матрицы и создаем ее
while True:
    m = input("Enter number of rows (>0): ")
    n = input("Enter number of columns (>0): ")
    if m.isdigit() and n.isdigit() and int(m) and int(n):
        matrix_rand = make_matrix(int(m), int(n))
        break
    print("You need to enter integer numbers > 0. Try again.")
# открываем файл или создаем новый и записываем в него матрицу
with open("task_18_1.json", "w") as file:
    file.write(json.dumps(matrix_rand))
# открываем файл на чтение и считываем оттуда матрицу
with open("task_18_1.json", "r") as file:
    data_from_file = file.read()
    matrix_from_file = json.loads(data_from_file)
# меняем считанную матрицу из файла согласно заданию
change_even_value(matrix_from_file)
# открываем файл или создаем новый и записываем в него обновленную матрицу
with open("task_18_2.json", "w") as file:
    file.write(json.dumps(matrix_from_file))
