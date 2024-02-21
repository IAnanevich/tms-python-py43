from datetime import datetime
from multiprocessing import Process


def function():
    l = []
    for i in range(10001):
        l.append(i)


if __name__ == '__main__':
    start = datetime.now()
    t1 = Process(target=function)
    t1.start()
    t1.join()
    time = datetime.now() - start
    print(time.total_seconds())
