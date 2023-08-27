# Создать матрицу случайных чисел и сохранить ее в json файл.
# После прочесть ее, обнулить все четные элементы и сохранить в другой файл
import json
import numpy as np

def matrix_def(matr):
    for i in range(len(matr)):
        for j in range(len(matr[i])):
            if matr[i][j] % 2:
                matr[i][j] = 0
    return matr

a = int(input('Введите количество столбцов: '))
b = int(input('Введите количество строк: '))

matrix_18 = np.random.randint(1, 100, (a, b))

with open("task_18_1.json", "w") as new_file:
    new_file.write(json.dumps(matrix_18))

with open("task_18.json", "r") as new_file:
    matrix_18_n = json.loads(new_file.read())

matrix_18_2 = matrix_def(matrix_18_n)

with open("task_18_2.json", "w") as new_file:
    new_file.write(json.dumps(matrix_18_2))








