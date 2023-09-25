# Дана целочисленная квадратная матрица. Найти в каждой строке наибольший
# элемент и поменять его местами с элементом главной диагонали.

matrix_list = [
    [8, 0, -16],
    [-12, -4, 8],
    [20, 12, 12]
]

matrix_list[1][1], matrix_list[1][2] = matrix_list[1][2], matrix_list[1][1]
matrix_list[2][0], matrix_list[2][2] = matrix_list[2][2], matrix_list[2][0]

# for elem in matrix_list[0]:
#     if matrix_list[0][0] <= max(matrix_list[0]):
#         matrix_list[0][0], matrix_list[0][0] = matrix_list[0][0], matrix_list[0][0]
#
# for elem in matrix_list[1]:
#     if matrix_list[1][0] <= max(matrix_list[1]):
#         matrix_list[1][1], matrix_list[1][2] = matrix_list[1][2], matrix_list[1][1]
#
# for elem in matrix_list[2]:
#     if matrix_list[2][0] <= max(matrix_list[2]):
#         matrix_list[2][0], matrix_list[2][2] = matrix_list[2][2], matrix_list[2][0]

print(matrix_list, '\n')
