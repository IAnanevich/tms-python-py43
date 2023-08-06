# Дан список. Создать новый список, сдвинутый на 1 элемент влево.
# Пример: 1 2 3 4 5 -> 2 3 4 5 1

number_list = [1, 2, 3, 4, 5]

first_number = number_list[0]  # забираем первый элемент, чтобы не затереть его

for i in range(len(number_list)):
    if i == len(number_list) - 1:
        number_list[i] = first_number
    else:
        number_list[i] = number_list[i + 1]

print(number_list)