'''
Ввести с клавиатуры целое число n. Получить сумму кубов всех целых чисел от 1 до
n(включая n). Реализовать в 2-х вариантах: используя цикл while и цикл for
'''

# for
print(sum([i**3 for i in range(1, int(input('Enter an integer: '))+1)]))

# while
n = int(input('Enter an integer: '))
summa = 0
while n := n-1:
    summa += n ** 3
print(summa)
