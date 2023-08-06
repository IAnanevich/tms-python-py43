# Ввести с клавиатуры целое целое число n. Получить сумму кубов всех целых чисел от 1 до n
# (включая). Реализовать в двух вариантах: используя оба цикла

i = 0
sum_1 = 0

number_1 = int(input('введите число m= '))
while i <= number_1:
    sum_1 += i**3
    i += 1
print(f'{sum_1}')

print('____________________________')

i = 0
sum_2 = 0

number_2 = int(input('введите число n= '))
spisok = []
while i <= number_2:
    spisok.append(i)
    i += 1
for i in spisok:
    sum_2 += i**3
    i += 1
print(f'{sum_2}')