def generator():
    first_number, second_number = 0, 1
    yield first_number
    yield second_number
    while True:
        result = first_number + second_number
        first_number = second_number
        second_number = result
        yield result


def write(n):
    gen = generator()
    for _ in range(n):
        print(next(gen))


try:
    count = int(input('How many times?\n'))
    write(count)
except Exception:
    print("Try again(")
