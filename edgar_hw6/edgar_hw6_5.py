# Написать декоратор к 2-м любым функциям, который бы считал и выводил время их выполнения.
# Подсказка: from datetime import datetime           time = datetime.now()
# ==============================================================================================

from datetime import datetime


def time_it(func):
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        result = func(*args, **kwargs)
        end_time = datetime.now()
        execution_time = end_time - start_time
        print(f'Time exception {func.__name__}: {execution_time}')
        return result

    return wrapper


# Example

@time_it
def example_function1():
    for _ in range(1000000):
        pass


@time_it
def example_function2():
    for _ in range(100000000):
        pass


# Call functions decorated with time_it decorator

example_function1()
example_function2()
