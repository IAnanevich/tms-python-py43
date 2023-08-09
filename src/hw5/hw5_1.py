# 1) Калькулятор на Python
# 5 функций (+, -, *, /, **)
# Цикл while как меню с выбором того, что хотим сделать
# ======================================================


def do_calc(math_operator: str, str_x: str, str_y: str) -> float | str:
    """
    :param math_operator: operation needed with x and y
    :param str_x: any number from input as text
    :param str_y: any number from input as text
    :return: result of calculation via operator and numbers
    """
    # try to convert
    if number_x.isdigit():
        x = float(str_x)
    else:
        x = 0

    # try to convert
    if number_y.isdigit():
        y = float(str_y)
    else:
        y = 0

    if math_operator == "+":
        return x + y
    elif math_operator == "-":
        return x - y
    elif math_operator == "*":
        return x * y
    elif math_operator == "/":
        if y == 0:
            return "Error: Division by 0"
        else:
            return x / y
    elif math_operator == "**":
        return x ** y
    else:
        # wrong operator chosen
        return "Error: wrong operator chosen"


while True:
    print("\nPlease enter any operator from list [+, -, *, /, **] or = to end calculations")
    operator = input(">> ")
    if operator not in ["+", "-", "*", "/", "**", "="]:
        continue

    if operator == "=":
        # user end calculations
        break
    else:
        # user continue calculations
        print("Please enter any number as X")
        number_x = input(">> ")
        print("Please enter any number as Y")
        number_y = input(">> ")
        print(f"\n{number_x} {operator} {number_y} = {do_calc(operator, number_x, number_y)}")
