import time


def get_current_time():
    """
    :return: '%H:%M:%S' time...
    """
    time.sleep(1)
    current_time = time.strftime('%H:%M:%S')
    return current_time


while True:  # endless cycle
    try:
        n = int(input("Enter the number"))
    except ValueError:
        print(f"invalid syntax")
    else:
        time_list = [get_current_time() for _ in range(n)]
        print(f"Список времени с задержкой:{time_list}")
        break  # exit cycle
