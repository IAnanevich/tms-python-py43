""" 5. Дан список. Создать новый список, сдвинутый на 1 элемент влево.
Пример: 1 2 3 4 5 -> 2 3 4 5 1 """

j = []
for i in range(5):
    number = input('Enter the number: ')
    j.append(number)
print(j)
imp = j[0]
j.pop(0)
j.append(imp)
print(j)
