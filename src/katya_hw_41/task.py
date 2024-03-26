# 1) В непустом массиве целых чисел nums, каждый элемент появляется дважды, кроме одного. Найдите его единственного.
# Сложность должна быть О(n)

def single_num(nums):
    result = 0
    for num in nums:
        result ^= num
    return result


print(single_num([2, 2, 1]))  # 1
print(single_num([3, 1, 2, 1, 2]))  # 3
print(single_num([1]))  # 1

# 2) Напишите алгоритм, определяющий, является ли число n счастливым.
# Счастливое число — это число, определяемое следующим процессом:
# Начиная с любого положительного целого числа, замените число суммой квадратов его цифр.
# Повторяйте процесс до тех пор, пока число не станет равным 1 (где оно и останется),
# или пока он не будет повторяться бесконечно в цикле, который не включает 1.
# Счастливыми являются те числа, для которых этот процесс заканчивается на 1.
# Вернит true, если n — счастливое число, и false, если нет.


def happy_num(n):
    set_1 = set()
    while n != 1 and n not in set_1:
        set_1.add(n)
        n = sum(int(m) ** 2 for m in str(n))
    return n == 1


print(happy_num(100))  # True
print(happy_num(178))  # False