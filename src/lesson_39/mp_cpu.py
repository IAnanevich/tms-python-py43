import multiprocessing
import time
import math


def calc(start, end):
    for i in range(start, end):
        math.factorial(i)


if __name__ == '__main__':
    start_time = time.time()

    limit = 10000
    num_processes = 20
    processes = []
    work_per_process = int(limit / num_processes)

    for i in range(1, limit, work_per_process):
        process = multiprocessing.Process(target=calc, args=(i, i + work_per_process))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    end_time = time.time() - start_time

    print(f'Время выполнения: {end_time:.3f} секунд')
