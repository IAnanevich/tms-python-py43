# Сделать функцию деление чисел и обернуть декоратором,
# который проверял бы деление на ноль и отказывал в работе пользователю


def forbidden_value(param_name: str, f_value: any, error_text: str):
    """
    Decorator function: pre-check argument for forbidden value. Print error text if check don't pass
    :param param_name: argument name that need to check
    :param f_value: forbidden value
    :param error_text: error message
    :return: result - if check pass / None - if value is forbidden
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            if kwargs.get(param_name) != f_value:
                return func(*args, **kwargs)
            print(error_text)
        return wrapper
    return decorator


@forbidden_value(param_name="divisor", f_value=0, error_text="Error: Division by 0")
def number_division(dividend: float, divisor: float) -> float:
    """
    Divide the dividend by divisor
    :param dividend: any float number
    :param divisor: any float number
    :return: result of division
    """
    return dividend / divisor


print(number_division(dividend=10, divisor=2))
print(number_division(dividend=10, divisor=0))
