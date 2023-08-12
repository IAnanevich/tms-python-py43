# Ввести с клавиатуры целое число n. Получить сумму кубов всех целых чисел от 1 до
# n(включая n). Реализовать в 2-х вариантах: используя цикл while и цикл for включая n).
# Реализовать в 2-х вариантах: используя цикл while и цикл for

# First method "WHILE"
# Enter n
n = int(input("Enter n: "))

sum_of_cubes = 0
current_num = 1

# Sum of cubes

while current_num <= n:
    sum_of_cubes += current_num ** 3
    current_num += 1

print(f'Sum of cubes for n = {n}: {sum_of_cubes}')

# -----------------------------------------------------------------------------------
# Second method "FOR"

m = int(input("Enter m: "))

sum_of_cubes1 = sum(num ** 3 for num in range(1, m + 1))

print(f'Sum of cubes for m = {m}: {sum_of_cubes1}')
