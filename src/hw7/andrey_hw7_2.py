# Ввести с клавиатуры 4 строки и сохранить их в 4 разные переменные.
# Создать файл и записать в него первые 2 строки и закрыть файл.
# Затем открыть файл на редактирование и доза писать оставшиеся 2 строки.
# В итоговом файле должны быть 4 строки, каждая из которых должна начинаться с новой строки.

if __name__ == "__main__":
    str_1 = input('Enter 1 line: ')
    str_2 = input('Enter 2 line: ')
    str_3 = input('Enter 3 line: ')
    str_4 = input('Enter 4 line: ')

    with open('example.txt', 'w') as f:
        f.write(f'{str_1}\n{str_2}\n')

    with open('example.txt', 'a') as f:
        f.write(f'{str_3}\n{str_4}')
