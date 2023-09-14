# Имеются два текстовых файла с одинаковым числом строк.Выяснить, совпадают
# ли их строки. Если нет, то получить номер первой строки, в которой эти
# файлы отличаются друг oт друга.

with open("task_17_1.txt") as file:
    data_1 = file.readlines()

with open("task_17_2.txt") as file:
    data_2 = file.readlines()

print(data_1)
print(data_2)

for i in range(len(data_1)):
    if data_1[i] != data_2[i]:
        print(i + 1)
        break
