# Имеется текстовый файл.
# Переписать в другой файл все его строки с заменой в них символа 0 на символ 1 и наоборот.

with open('task_string.txt') as f:
    with open('task_string_2.txt', 'w') as file:
        s = ''
        for line in f.readline():
            if line == "1":
                s += "0"
            elif line == "0":
                s += "1"
            else:
                s += line
        for line in f.readline():
            if line == "1":
                s += "0"
            elif line == "0":
                s += "1"
            else:
                s += line
        file.write(s)
