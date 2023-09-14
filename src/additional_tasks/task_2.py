# Два натуральных числа называют дружественными, если каждое из них равно
# сумме всех делителей другого, кроме самого этого числа. Найти все пары
# дружественных чисел, лежащих в диапазоне от 200 до 300.

list_2 = list(range(200, 301))
print(list_2)


def find_all_div(n, k=0):
    for i in list(range(1, int(n / 2) + 1)):
        if n % i == 0:
            k += i
    return k


for i in list_2:
    for j in list_2:
        if i == find_all_div(j):
            print(f"{i} и {j}")
