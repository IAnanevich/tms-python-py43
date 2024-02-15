import time
import math


def calc(number):
    math.factorial(number)


start_time = time.time()

for i in range(1, 10000):
    calc(i)

end_time = time.time() - start_time
print(f'Время выполнения: {end_time:.3f} секунд')
