# калькулятор
import re


def calculator(operator: str, x: float, y: float) -> float:
    if operator == "+":
        return x + y
    elif operator == "-":
        return x - y
    elif operator == "*":
        return x * y
    elif operator == "/":
        if y == 0:
            return "Ошибка! Деление на 0"
        return x / y
    elif operator == "**":
        return x ** y

def prepare_num(num):
    num = re.sub("[^0-9.-]", "", num)

    if len(num) == 0 or (len(num) == 1 and num in [".", "-"]):
        return 0

    if num[0] == ".":
        num = "0" + num
    elif num[0:2] == "-.":
        num = "0" + num[1:]

    # удаляем все минусы если минус стоит не на первом месте
    if num.rfind("-") > 0:
        num = num.replace("-", "")

    # удаляем все точки их больше одной
    if num.count('.') > 1:
        num = num.replace(".", "")

    num = float(num)
    return num

while True:
    operator_name = {"+": "плюс", "-": "минус", "/": "разделить", "*": "умножить", "**": "в степени"}
    operator = input("Введите оператор. доступные варианты " + ", ".join(operator_name.keys()) + ", q - exit: ")

    if(operator == "q"):
        break
    if operator not in ["+", "-", "/", "*", "**"]:
        continue

    x = input("Введите x: ")
    y = input("Введите y: ")

    x = prepare_num(x)
    y = prepare_num(y)

    result = calculator(operator, x, y)
    print(f"Результат = {x} {operator_name[operator]} {y} = {result}")
