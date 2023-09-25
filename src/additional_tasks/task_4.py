# В массиве целых чисел с количеством элементов 19 определить максимальное
# число и заменить им все четные по значению элементы. Использовать рандом для
# заполнения цикла элементами, диапазон рандома принимать от пользователя

from random import randint

n = int(input())
new_list = []
for i in range(19):
    new_list.append(randint(1,n))
    m = max(new_list)
    if new_list[i] % 2 == 0:
        print(f'{new_list[i]}',end=' ')
        new_list[i] = m

print('\n')
print(new_list)
print(f'max number is = {m}')
