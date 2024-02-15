from threading import Thread, Event
from time import sleep

event = Event()


def worker(name):
    event.wait()
    print(f'Worker: {name}')


event.clear()

workers = [Thread(target=worker, args=(f'worker {i}', )) for i in range(5)]

for w in workers:
    w.start()

sleep(2)
print('Main thread')
event.set()
