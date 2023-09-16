# Дан произвольный список некоторых целых чисел,
# найдите значение 20 в нем и если оно присутствует, замените его на 200.
# Обновите список только при первом вхождении числа 20"""

numbers_before = [10, 20, 20, 30, 40, 50, 20]
print(f"Before: {numbers_before}")

for i in range(0, len(numbers_before)):
    if numbers_before[i] == 20:
        numbers_before[i] = 200
        break

print(f"After: {numbers_before}")
