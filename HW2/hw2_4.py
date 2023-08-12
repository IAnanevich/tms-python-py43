# Пользователь вводит два числа n и х.
# Нужно вывести на экран число х ровно n раз в формате [х, х, … , х].

print("\nPlease enter X")
some_input = input(">> ")
if some_input.isdigit():
    x = int(some_input)
else:
    x = 100

print("\nPlease enter Y")
some_input = input(">> ")
if some_input.isdigit():
    y = int(some_input)
else:
    y = 5

result = []
for i in range(0, y):
    result.append(x)

print(result)
