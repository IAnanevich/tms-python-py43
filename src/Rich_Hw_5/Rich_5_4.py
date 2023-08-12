import time

def get_current_time():
    time.sleep(1)
    current_time = time.strftime('%H:%M:%S')
    return current_time


n = int(input("Введите чето "))
time_list = [get_current_time() for _ in range(n)]
print("Список времен с задержкой:")
print(time_list)
