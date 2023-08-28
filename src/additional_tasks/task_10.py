# Дан список строк. Отформатировать все строки в формате {i}-{string}, где i это
# порядковый номер строки в списке. Использовать генератор списков.

def format_list_of_string(list_of_string: list) -> list:
    """ Return formatted strings in the list in the format {i}-{string},
        where i is the ordinal number of the string in the list.

    :param list_of_string: list of words
    :return: list of formatted words
    """
    return [f"{list_of_string.index(i)}-{i}" for i in list_of_string]


if __name__ == "__main__":
    print(format_list_of_string(["one", "two", "three", "four"]))
