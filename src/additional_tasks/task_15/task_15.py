# Имеется текстовый файл.
# Переписать в другой файл все его строки
# с заменой в них символа о на символ а и наоборот.

f3 = open("task_15.txt")
fd = f3.readlines()


def replacer(strings):
    for i in range(len(strings)):
        strings[i] = strings[i].replace("о", "А")
        list_15.append(strings[i])
    return list_15


list_15 = []
fd_new = replacer(fd)
fd_n = "\n".join(fd_new)
print(fd_new)

f6 = open("task_15_new.txt", "w")
f6.write(f"{fd_n}")
f6.close()
