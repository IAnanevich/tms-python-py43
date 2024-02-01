import time
import math


if __name__ == '__main__':
    start_time = time.time()
    math.factorial(1000000)
    end_time = time.time() - start_time

    print(f'Sync factorial: {end_time:.5f} seconds')

