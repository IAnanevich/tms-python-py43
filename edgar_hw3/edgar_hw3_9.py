# Составить список чисел Фибоначчи содержащий 15 элементов.
# (Подсказка: Числа Фибоначчи - последовательность, в которой первые два числа
# равны либо 1 и 1, а каждое последующее число равно сумме двух предыдущих
# чисел. Пример: 1, 1, 2, 3, 5, 8, 13, 21, 34... )

# number of item in the list
n = 15

fibonacci_list = [1, 1]

for i in range (2,n):
    next_fibonacci = fibonacci_list[-1] + fibonacci_list[-2]
    fibonacci_list.append(next_fibonacci)
print("List Fibonacci: ", fibonacci_list)
