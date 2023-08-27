# Имеются два текстовых файла с одинаковым числом строк. Выяснить, совпадают ли их строки.
# Если нет, то получить номер первой строки, в которой эти файлы отличаются друг от друга.


def find_different_string(text_1: list[str], text_2: list[str]) -> None:
    """
    find number of first different string in texts
    :param text_1: first text
    :param text_2: second text
    :return: None
    """
    # список поэлементного сравнения списков: 0 - строки совпадают, номер строки (нумерация с 1) - если отличаются
    my_pr = [0 if text_1[i] == text_2[i] else i + 1 for i in range(len(text_1))]
    if sum(my_pr):
        print("Files aren't identical.")
        # номер первой отличающейся строки
        print(f"First different string is {list(filter(lambda x: x > 0, my_pr))[0]}.")
    else:
        print("Files are identical.")


# считываем строки из файлов
with open("task_17_1.txt", "r") as file_1, open("task_17_2.txt", "r") as file_2:
    text_read_1 = file_1.readlines()
    text_read_2 = file_2.readlines()
# проверка на отличия
find_different_string(text_read_1, text_read_2)
# Files aren't identical.
# First different string is 4.
