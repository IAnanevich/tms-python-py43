# Написать декоратор к 2-м любым функциям, который бы считал и выводил время их выполнения.
# Подсказка:
#   from datetime import datetime
#   time = datetime.now()
from time import sleep
from datetime import datetime


def stopwatch(func):
    """
    Stopwatch the function time and print delta time
    """
    def inner(*args, **kwargs):
        start_time = datetime.now()
        result = func(*args, **kwargs)
        print(f"Time spend: {datetime.now() - start_time}")
        return result
    return inner


@stopwatch
def snooze(seconds: float) -> None:
    """
    Just sleep for a moment ;)
    :param seconds: seconds to wait
    :return: None
    """
    sleep(seconds)


@stopwatch
def theorem(number: int) -> list:
    """
    # Theorem 3x + 1
    # The 3x+1 problem, concerns the behavior of the iterates of the function which takes odd integers n to 3n+1
     and even integers n to n/2.
    # The 3x+1 conjecture asserts that, starting from any positive integer n,
     repeated iteration of this function eventually produces the value 1.
    :param number: any int number
    :return: list of steps
    """

    # Steps already passed
    steps = 0

    # Steps history
    history = [float]

    # Let's check the input X
    if number == 1:
        # Already 1
        s = number
        history.append(s)
    else:
        # Run function 3x+1
        s = 3 * number + 1
        steps += 1
        history.append(s)

    while s != 1:
        sleep(0.001)
        # odd or even
        if (s / 2) != round(s / 2, 0):
            # odd integers 3x+1
            steps += 1
            s = 3 * s + 1
            history.append(s)
        else:
            # even integers x/2
            steps += 1
            s = s / 2
            history.append(s)
    return history


print("\nsnooze 1.3 sec")
snooze(seconds=1.3)

print("\ntheorem(5156456465)")
theorem(number=5156456465)
