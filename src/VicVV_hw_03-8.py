#Дан список. Создать новый список, сдвинутый на 1 элемент влево. Пример: 1 2 3 4
# 5 -> 2 3 4 5 1
list_1 = [1, 2, 4, 6, 7, 8, 3]
while 1:
    list_1.append(list_1[0])
    list_1.pop(0)
    print(list_1)
    if input('ещё? (y)') != 'y':
        break


