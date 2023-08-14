# Составить список чисел Фибоначчи содержащий 15 элементов.
# Подсказка:
# Числа Фибоначчи - последовательность, в которой первые два числа равны либо 1 и 1,
# а каждое последующее число равно сумме двух предыдущих чисел.
# Пример: 1, 1, 2, 3, 5, 8, 13, 21, 34... )

print("\nСоставим список чисел Фибоначчи содержащий 15 элементов")
print("\nС какого числа начнем?")

start_number = 1
some_value = input('>> ')
try:
    start_number = int(some_value)
except ValueError:
    print("Ясно... начнем с 1")
    start_number = 1
finally:
    if start_number < 1:
        print("Ясно... начнем с 1")
        start_number = 1

# первые два числа равны либо 1 и 1
numbers = list()
numbers.append(start_number)
numbers.append(start_number)

# Оставшиеся 13 чисел
for i in range(2, 15):
    # каждое последующее число равно сумме двух предыдущих чисел
    numbers.append(numbers[i-1] + numbers[i-2])

print("\nСписок чисел Фибоначчи содержащий 15 элементов начиная с ", start_number)
print(numbers)
