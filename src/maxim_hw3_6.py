# Дан список целых чисел. Подсчитать сколько четных чисел в списке.

print(sum(1 for i in [0, 11, 22, 13, 5, 99, 100, 10, 8] if not i % 2))
