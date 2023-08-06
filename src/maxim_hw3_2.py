# Ввести с клавиатуры целое число n. Получить сумму кубов всех целых чисел # от 1
# до n(включая n). Реализовать в 2-х вариантах: используя цикл while и цикл for.

n = int(input("Enter an integer: "))
# цикл for
print(sum(i**3 for i in range(1, n+1)))
# цикл while
number, answer = 1, 0
while number <= n:
    answer += number ** 3
    number += 1
else:
    print(answer)
