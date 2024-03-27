import time

my_list = []


def add_list(number: int) -> None:
    my_list.append(number)


start_time = time.time()

for i in range(1, 10001):
    add_list(i)

finish_time_cpu = time.time()-start_time
print(f'Время выполнения "CPU" {finish_time_cpu:.5f} ')  # 0.00104
# print(f'Время выполнения "MT_CPU" {finish_time:.5f} ')  # 0.39352
# print(f'Время выполнения "MP_CPU" {finish_time:.5f} ')  # 0.12827


