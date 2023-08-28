# Дана целочисленная квадратная матрица. Найти в каждой строке наибольший
# элемент и поменять его местами с элементом главной диагонали.

def change_matrix(matrix: list) -> list:
    """ Return a matrix in which the main diagonal contains the maximum elements.

    :param matrix: integer square matrix
    :return: integer square matrix
    """
    for lst in matrix:
        ind, max_elem = matrix.index(lst), max(lst)
        lst[lst.index(max_elem)], lst[ind] = lst[ind], max_elem
    return matrix


if __name__ == "__main__":
    for i in change_matrix([[0, 0, 1], [-12, -14, -8], [20, 12, 12]]):
        print(i)
