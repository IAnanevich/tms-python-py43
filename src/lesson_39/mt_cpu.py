import threading
import time
import math


def calc(number):
    math.factorial(number)


start_time = time.time()
threads = []

for i in range(1, 10000):
    thread = threading.Thread(target=calc, args=(i,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

end_time = time.time() - start_time
print(f'Время выполнения: {end_time:.3f} секунд')
