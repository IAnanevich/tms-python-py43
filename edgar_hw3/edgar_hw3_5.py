# Дан список целых чисел.
# Создать новый список, каждый элемент которого равен исходному элементу
# умноженному на -2

original_list = [1, 2, 3, 4, 5]

new_list = [-2 * num for num in original_list]

print("New list: ", new_list)
