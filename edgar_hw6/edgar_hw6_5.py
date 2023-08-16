# Написать декоратор к 2-м любым функциям, который бы считал и выводил время их выполнения.
# Подсказка: from datetime import datetime           time = datetime.now()
# ==============================================================================================
import time
from datetime import datetime


def time_it(func):
    """
    A decorator that measures the execution time of a function.
    :param func: Function whose execution time is to be measured
    :return: Wrapped function with added time measurement
    """
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        result = func(*args, **kwargs)
        print(f'Time exception {func.__name__}: {datetime.now() - start_time}')
        return result

    return wrapper

# Example

@time_it
def example_function1():
    """
    Example of function 1 with a delay of 1 second.
    """
    for _ in range(1000000):
        pass
    time.sleep(1)

@time_it
def example_function2():
    """
    Example of function 2
    """
    for _ in range(100000000):
        pass

# Call functions decorated with time_it decorator

example_function1()
example_function2()
