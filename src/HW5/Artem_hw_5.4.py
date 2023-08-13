from datetime import datetime
import time

def list_numbers(n):
    """гениратор списка"""
    new_list = []
    for i in range(1, n):
        new_list.append(datetime.strftime(datetime.now(time.sleep(1)),'%Y-%m-%d %H:%M:%S'))
    return new_list


n = int(input())
print(list_numbers(n))
