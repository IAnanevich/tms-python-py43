from time import sleep


def fib(n):
    a, b = 1, 1
    for i in range(n):
        yield a
        a, b = b, a + b


gen = fib(10)
for numbers in gen:
    print(numbers)

print(list(fib(10)))
