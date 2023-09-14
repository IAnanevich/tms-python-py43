# Для каждого натурального числа в промежутке от m до n
# вывести все делители, кроме единицы и самого числа.
# m и n вводятся с клавиатуры.


n = int(input("Введите нижнюю границу диапозона "))
m = int(input("Введите верхнюю границу диапозона "))

list_2 = list(range(n, m + 1))
print(list_2)
list_div = []


def find_all_div(n):
    for i in range(1, n + 1):
        if n % i == 0:
            list_div.append(i)
    return list_div


for i in list_2:
    print(f"Делители числа {i} - {find_all_div(i)}")
    list_div = []
