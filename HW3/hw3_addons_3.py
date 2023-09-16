# Дан список целых чисел.
# Подсчитать сколько четных чисел в списке

numbers = [1, 2, 3, 3, 4, 5, 6, 6, 8, 9]
even_numbers = [i for i in numbers if not i % 2]

print("В списке ", numbers)
print(len(even_numbers), " четных числа (ел) и это ", even_numbers)
