# Задан целочисленный массив. Определить количество участков массива,
# на котором элементы монотонно возрастают (каждое следующее число больше
# предыдущего).
import numpy as np

list_5 = list(np.random.randint(100, 300, 20))

print(list_5)
pass_list = False

count_mas = 0
for i in range(len(list_5)):
    if i < len(list_5) - 1 and (list_5[i] < list_5[i + 1]):
        count_mas += 1
print(count_mas)
