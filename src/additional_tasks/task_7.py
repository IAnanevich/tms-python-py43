# В заданной строке расположить в обратном порядке все слова. Разделителями
# слов считаются пробелы. (сделать используя .split())

def reverse_string(initial_string: str) -> str:
    """ Return a string in which all the words in reverse order.

    :param initial_string: given string
    :return: string in reverse order
    """
    return " ".join(initial_string.split()[::-1])


if __name__ == "__main__":
    input_string = input("Enter a sentence: ")
    print(reverse_string(input_string))
