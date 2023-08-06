# Ввести с клавиатуры целое число n. Получить сумму кубов всех целых чисел от 1 до n(включая n).
# Реализовать в 2-х вариантах: используя цикл while и цикл for

n = int(input('Enter number:'))
sum_third_power = 0  # пустышка для суммирования

for i in range(1, n + 1):
    sum_third_power += i ** 3

# while n:  # считаем, что оно нам больше не понадобится
#     sum_third_power += n ** 3
#     n -= 1

print(sum_third_power)