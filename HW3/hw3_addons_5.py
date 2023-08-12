# Дан список.
# Создать новый список, сдвинутый на 1 элемент влево.
# Пример: 1 2 3 4 5 -> 2 3 4 5 1


numbers_before = [1, 2, 3, 4, 5]
numbers_after = numbers_before[1:] + numbers_before[:1]

print(f"Before: {numbers_before}")
print(f"After: {numbers_after}")
