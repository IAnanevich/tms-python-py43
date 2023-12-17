# Составить список чисел Фибоначчи содержащий 15 элементов.
# (Подсказка: Числа Фибоначчи - последовательность, в которой первые два числа
# равны либо 1 и 1, а каждое последующее число равно сумме двух предыдущих чисел.
# Пример: 1, 1, 2, 3, 5, 8, 13, 21, 34... )

# n = 15
n = int(input("Enter length Fibonacci list: "))
# fib_list = list(range(n))
fib_list = [1]  # полагаем, что введут нормальное число
a = 0
b = 1

# for i in range(n):
#     if i < 2:
#         fib_list[i] = 1
#     else:
#         fib_list[i] = fib_list[i - 1] + fib_list[i - 2]
#
# print(*fib_list, sep=', ')

while n - 1:
    a, b = b, a + b
    fib_list.append(b)
    n -= 1

print(*fib_list, sep=', ')
