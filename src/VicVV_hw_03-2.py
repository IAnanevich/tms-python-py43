# Получить сумму кубов всех целых чисел от 1 до n, включая n.
# Реализовать в 2-х вариантах: используя цикл while и цикл for

n = input("Введите целое число:")
if not n.isdigit():
    print('это не число')
elif int(n) != float(n):
    print('это не целое число')
else:
    rez = 0
    for counter in range(int(n) + 1):
        rez += counter**3
    print(f'v.1: сумма кубов чисел от 1 до {n} равна {rez}')
    rez = 0
    counter = 1
    while counter != int(n) + 1:
        rez += counter**3
        counter += 1
    print(f'v.2: сумма кубов чисел от 1 до {n} равна {rez}')
