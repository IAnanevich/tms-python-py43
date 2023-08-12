# Ввести с клавиатуры целое число n.
# Получить сумму кубов всех целых чисел от 1 до n (включая n).
# Реализовать в 2-х вариантах: используя цикл while и цикл for

print("\nВведите с клавиатуры целое число")
n = int(input('>> '))

result = 0
for x in range(1, n + 1):
    result += x ** 3

print("for x in range(1, n + 1)")
print(result)

result = 0
while n:
    result += n ** 3
    n -= 1

print("while n: n -= 1")
print(result)
