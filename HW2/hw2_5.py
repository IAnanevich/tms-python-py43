# Дан список [10, 15, 1, 15, 10, 1, 6, 6, 15, 11, -4, -10, -10].
# Удалить из него все повторяющиеся значения.

numbers_before = [10, 15, 1, 15, 10, 1, 6, 6, 15, 11, -4, -10, -10]
print(f"Before: {numbers_before}")

numbers_after = list(set(numbers_before))
print(f"After: {numbers_after}")
