"""2. Дан список целых чисел.
Создать новый список, каждый элемент которого равен исходному элементу
умноженному на -2"""

i = int(input('Enter the number of values is in the list: '))
without = []
with_2 = []
for b in range(i):
    x = int(input('Enter a value into the list: '))
    without.append(x)
    with_2.append(x * -2)
print(without)
print(with_2)
