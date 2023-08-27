# Имеется текстовый файл. Все четные строки этого файла записать во второй
# файл, а нечетные — в третий файл. Порядок следования строк сохраняется

flag = -1  # признак номера строки: меньше нуля - четная строка, больше - нечетная
with open("task_16.txt", "r") as file:
    str_read = file.readlines()
    # перебираем все строки и в зависимости от из номера дополняем нужный файл(норм каждый раз открывать?)
    for st in str_read:
        flag *= -1
        if flag < 0:
            with open("task_16_2.txt", "a") as file_work:
                file_work.write(st)
        else:
            with open("task_16_3.txt", "a") as file_work:
                file_work.write(st)
