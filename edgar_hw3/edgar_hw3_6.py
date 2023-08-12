# Дан список целых чисел. Подсчитать сколько четных чисел в списке

numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

even_count = sum(1 for num in numbers_list if num % 2 == 0)
print("Even count: ", even_count)
