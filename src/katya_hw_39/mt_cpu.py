import time
import threading

my_list = []


def add_list(number: int) -> None:
    my_list.append(number)


start_time = time.time()
threads =[]

for i in range(1, 10001):
    thread = threading.Thread(target=add_list, args=(i,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

finish_time = time.time()-start_time
print(f'Время выполнения "MT_CPU" {finish_time:.5f} ')  # 0.39352
# print(f'Время выполнения "CPU" {finish_time_cpu:.5f} ')  #0.00104
# print(f'Время выполнения "MP_CPU" {finish_time:.5f} ')  # 0.12827
