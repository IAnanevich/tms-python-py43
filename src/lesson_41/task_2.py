def is_square_number_optimized(num):
    # Проверка, что число неотрицательное
    if num < 0:
        return False

    # Бинарный поиск для нахождения квадратного корня
    left, right = 0, num
    while left <= right:
        mid = (left + right) // 2
        mid_squared = mid * mid

        if mid_squared == num:
            return True
        elif mid_squared < num:
            left = mid + 1
        else:
            right = mid - 1

    return False


# Пример использования:
num = 101
if is_square_number_optimized(num):
    print(f"{num} - является квадратом другого числа")
else:
    print(f"{num} - не является квадратом другого числа")
