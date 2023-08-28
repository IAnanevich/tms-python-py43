# Задан целочисленный массив. Определить количество участков массива, на
# котором элементы монотонно возрастают (каждое следующее число больше предыдущего).

def find_sections(check_list: list, count_areas: int = 0) -> int:
    """ Return the number of array sections in which elements are monotonically increasing.

    :param check_list: array to search
    :param count_areas: quantity of sections
    :return: quantity of sections
    """
    length = len(check_list)
    next_id = 1
    area = False
    while length > next_id:
        if check_list[next_id - 1] >= check_list[next_id]:
            return find_sections(check_list[next_id:], count_areas)
        elif not area:
            count_areas += 1
            area = True
        next_id += 1
    return count_areas


if __name__ == "__main__":
    print(find_sections([1, 2, 3, 4, 5, 6, 6, 7, 8, 9, 10, 11, 7]))
