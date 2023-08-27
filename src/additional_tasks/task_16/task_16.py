# Имеется текстовый файл. Все четные строки этого файла
# записать во второй файл, а нечетные — в третий файл.
# Порядок следования строк сохраняется.

with open("task_16.txt") as file:
    data = file.readlines()

res_1 = ""
res_2 = ""

for i in range(len(data)):
    if i % 2 == 0:
        res_1 += f"{data[i]}"
    else:
        res_2 += f"{data[i]}"


f9 = open("task_16_1.txt", "w")
f9.write(f"{res_1}")
f9.close()

f10 = open("task_16_2.txt", "w")
f10.write(f"{res_2}")
f10.close()
