#Дан список целых чисел. Подсчитать сколько четных чисел в списке
spis = [10, 15, 1, 15, 10, 1, 6, 6, 15, 11, -4, -10, -10]

spis = list(range(len(spis)))
print(spis[::2])
spis = spis[::2]
print(len(spis))
