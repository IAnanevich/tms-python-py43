# Создать программу, которая добавляет в список числа от 0 до 10000.
#
# a. без потоков и процессов
# b. С помощью потоков
# c. С помощью процессов
# d. Сравнить все 3 варианта

from marina_hw39_regular import make_array_regular
from marina_hw39_thread import make_array_thread
from marina_hw39_process import make_array_process

if __name__ == "__main__":
    n = 10000
    # время работы обычной программы
    regular_time = make_array_regular(n)
    print(f"Regular_time is: {regular_time:.6f} seconds")
    # время работы потоковой программы
    threads_time = make_array_thread(n)
    print(f"Thread_time is: {threads_time:.6f} seconds")
    # время работы процессорной программы
    processes_time = make_array_process(n)
    print(f"Process_time is: {processes_time:.6f} seconds")
