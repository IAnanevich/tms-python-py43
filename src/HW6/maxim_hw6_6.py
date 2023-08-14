# Сделать функцию которая на вход принимать строку. Анализирует ее
# исключительно методом isdigit() без доп. библиотек и переводит строку в число.
# Функция умеет распознавать отрицательные числа и десятичные дроби. Примеры:
# -6.7  -> Вы ввели отрицательное дробное число: -6.7
# 5     -> Вы ввели положительное целое число: 5
# 5.4r  -> Вы ввели не корректное число: 5.4r
# -.777 -> Вы ввели отрицательное дробное число: -0.777

def check_numeric(digit_str: str) -> str:
    """
    Return of a recognized number or incorrect entry

    :param digit_str: number by string
    :return: format string
    """
    list_trues = list(map(lambda x: x.isdigit(), digit_str.strip()))
    f, t = list_trues.count(False), list_trues.count(True)
    answer = f"You entered an incorrect number: {digit_str}"
    while 1:
        if t == 0 or f == 0 and t == 0 or f > 2:
            break
        elif f > 1:
            try:
                res = float(digit_str)
            except ValueError:
                break
            answer = f"You entered a negative float: {res}"
            break
        elif f == 1:
            try:
                res = int(digit_str)
            except ValueError:
                try:
                    res = float(digit_str)
                except ValueError:
                    break
                answer = f"You entered a positive float: {res}"
                break
            answer = f"You entered a negative integer: {res}"
            break
        else:
            answer = f"You entered a positive integer: {int(digit_str)}"
            break
    return answer


if __name__ == "__main__":
    print(check_numeric(input("Enter numeric: ")))
