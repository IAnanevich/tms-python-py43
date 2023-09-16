# 1) Калькулятор на Python
# 5 функций (+, -, *, /, **)
# Цикл while как меню с выбором того, что хотим сделать
# ======================================================


def do_calc(math_operator: str, str_x: str, str_y: str) -> float | str:
    """
    Do math calculation by selected math operator from list [+, -, *, /, **]
    :param math_operator: operation needed with x and y
    :param str_x: any number from input as text
    :param str_y: any number from input as text
    :return: result of calculation via operator and numbers
    """
    # try to convert
    try:
        x = float(str_x)
    except ValueError as e:
        print(f"X = 0, because of {e}")
        x = 0

    # try to convert
    try:
        y = float(str_y)
    except ValueError as e:
        print(f"Y = 0, because of {e}")
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
        print(f"\n{number_x} {operator} {number_y} = {do_calc(math_operator=operator, str_x=number_x, str_y=number_y)}")
