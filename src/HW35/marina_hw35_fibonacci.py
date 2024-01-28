# Написать генератор чисел Фибоначчи
from typing import Iterator, Generator


def gener_fibonacci_number(n: int) -> Iterator[int]:
    """
    n-number Fibonacci's sequence
    :param n: Fibonacci base
    """
    numb_1, numb_2 = 0, 1
    for _ in range(n):
        numb_1, numb_2 = numb_2, numb_1 + numb_2
    yield numb_2 - numb_1


def gener_fibonacci_sequence(n: int) -> Generator[int, None, None]:
    """
    Fibonacci's sequence length n
    :param n: Fibonacci base
    """
    numb_1, numb_2 = 0, 1
    for _ in range(n):
        yield numb_1
        numb_1, numb_2 = numb_2, numb_1 + numb_2


while True:
    print("\n *** What do you want to do?")
    print(
        "1. Get a N-Fibonacci number",
        "2. Get a Fibonacci's sequence",
        "0. Exit",
        sep="\n",
    )
    action_s = input("Please enter operation: ")
    if action_s.isdigit():
        action = int(action_s)
        if not action:
            print("Goodbye!")
            break
        elif action in [1, 2]:
            while True:
                fib_numb_s = input("Enter N - an integer number: ")
                if fib_numb_s.isdigit():
                    if action == 1:
                        print(
                            f"{fib_numb_s}th Fibonacci's number is: ",
                            *gener_fibonacci_number(int(fib_numb_s)),
                        )
                        break
                    if action == 2:
                        print(f"Fibonacci's sequence length {fib_numb_s} is: ")
                        print(*gener_fibonacci_sequence(int(fib_numb_s)))
                        break
                else:
                    print("!!!You need to enter number, try again")
        else:
            print("\n!!!Choose correct number")
    else:
        print(
            "!!!You need to enter integer NUMBER to choose operation not String, try again"
        )
