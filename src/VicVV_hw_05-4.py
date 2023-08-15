# 4 генератор списка из дат

from datetime import datetime


def get_list(sec: int) -> list:
    time_start = datetime.timestamp(datetime.now())
    list_d = []
    for s in range(0, sec):
        d = datetime.fromtimestamp(time_start + s)
        list_d.append(datetime.strftime(d, "%Y-%m-%d %H:%M:%S"))
    return list_d


ss = int(input("Сколько элементов списка? "))
print(get_list(ss))
