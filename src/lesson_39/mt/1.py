from threading import Thread
from time import sleep
from queue import Queue


numbers = []


def func(queue):
    for i in range(5):
        print(f'from child thread: {i}')
        sleep(0.5)
        queue.put(i ** 2)


queue = Queue()

th1 = Thread(target=func, args=(queue,))
# th2 = Thread(target=func, args=(queue,))

print(th1.is_alive())

th1.start()
# th2.start()

print(th1.is_alive())

sleep(4.0)

print(th1.is_alive())

# th1.join()
# th2.join()
# func()

# while not queue.empty():
#     print(f'from main thread: {queue.get()}')
#     sleep(1.0)
