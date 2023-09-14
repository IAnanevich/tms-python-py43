# Дана целочисленная квадратная матрица. Найти в каждой строке наибольший
# элемент и поменять его местами с элементом главной диагонали.


matrix_6 = [
    [-11, 1, 20],
    [19, -1, 10],
    [18, 18, -1],
]

for i in range(len(matrix_6)):
    max_num = max(matrix_6[i])
    for j in range(len(matrix_6[i])):
        if matrix_6[i][j] == max_num:
            matrix_6[i][j] = matrix_6[i][i]
            matrix_6[i][i] = max_num

for i in matrix_6:
    print(i)
