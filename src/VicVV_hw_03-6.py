#Дан список целых чисел. Подсчитать сколько четных чисел в списке
list_1 = [2, 4, 6, 7, 8, 3]
count = 0
for l in list_1:
    if l % 2 == 0:
        count = count + 1
print(f' в списке четных {count}')
