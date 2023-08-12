# 3. Дан список целых чисел. Подсчитать сколько четных чисел в списке

i = int(input('Enter the number of values is in the list: '))
w = []
c = 0
for b in range(i):
    x = int(input('Enter a value into the list: '))
    w.append(x)
print(w)
for b in w:
    if b % 2 == 0:
        c += 1
print(f'Even numbers : {c}')
