# Дан список целыз чисел. Создать список, каждый элемент которого равен искодному
# элементу умноженному на 2

list_3 = [5, 8, 9, -4, 0, -3]
i = 0
list_4 = []

# while i < len(list_3):
#     list_4.append(list_3[i] * 2)
#     i += 1
# else:
#     print(f'{list_4}')

for i in list_3:
    list_4.append(i * 2)
print(f'{list_4}')