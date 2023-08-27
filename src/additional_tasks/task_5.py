# Задан целочисленный массив. Определить количество участков массива,
# на котором элементы монотонно возрастают
# (каждое следующее число больше предыдущего).

from itertools import groupby
s = ''
list_a = [90, 65, 1, 2, 3, 4, 18, 18, 10, 11, 12, 13, 14, 15, 45, 19, 16, 20,21,22,23,24]

for i in range(0, len(list_a) - 1):
    if list_a[i] < list_a[i + 1]:
        s += '+'
        print(list_a[i], end=' ')
    else:
        s += '-'
g = groupby(s)
out = [k for k,v in g if k=='+']
print('result:',len(out))
