import time
import multiprocessing

my_list = []


def add_list(start: int, end: int) -> None:
    for i in range(start, end):
        my_list.append(i)


if __name__ == '__main__':
    start_time = time.time()

    limit = 10001
    processes = []
    num_processes = 8
    work_per_process = int(limit/num_processes)

    for i in range(1, limit, work_per_process):
        process = multiprocessing.Process(target=add_list, args=(i,i+work_per_process))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    finish_time = time.time()-start_time
    print(f'Время выполнения "MP_CPU" {finish_time:.5f} ')  # 0.12827
    # print(f'Время выполнения "CPU" {finish_time_cpu:.5f} ')  # 0.00104
    # print(f'Время выполнения "MT_CPU" {finish_time:.5f} ')  # 0.39352
