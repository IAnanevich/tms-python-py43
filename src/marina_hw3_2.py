# Дан список целых чисел.
# Создать новый список, каждый элемент которого равен исходному элементу, умноженному на -2.

number_list = [1, 2, 3, 4, 5, 6, 7]
double_number_list = [ - 2 * i for i in number_list]
print(double_number_list)
