# Дан список целых чисел.
# Создать новый список, каждый элемент которого равен исходному элементу
# умноженному на -2

numbers_before = [1, 2, 3, 3, 4, 5]
numbers_after = [n * -2 for n in numbers_before]

print(f"Before: {numbers_before}")
print(f"After: {numbers_after}")
