# Дан список чисел.
# Вернуть список, где при помощи функции map() каждое число переведено в строку.
# В качестве функции в map использовать lambda

numbers = [0, 1, 2, 3, 4, 5]
strings = list(map(lambda i: str(i), numbers))

print(numbers)
print(strings)
