import time


def get_current_time() -> str:
    """
    :return: '%H:%M:%S' time...
    """
    time.sleep(1)
    return time.strftime('%H:%M:%S')


while True:  # endless cycle
    try:
        n = int(input("Enter the number"))
    except ValueError:
        print(f"invalid syntax")
    else:
        time_list = [get_current_time() for _ in range(n)]
        print(f"Список времени с задержкой:{time_list}")
        break  # exit cycle
