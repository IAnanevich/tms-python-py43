# Дан список. Создать новый список, сдвинутый на 1 элемент влево. Пример: 1 2 3 4
# 5 -> 2 3 4 5 1

original_list = [1, 2, 3, 4, 5]

shifted_list = original_list[1:]+[original_list[0]]

print("New List: ", shifted_list)
