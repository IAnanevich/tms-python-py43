import threading


def task():
    print('Hello world')


timer = threading.Timer(5, task)
timer.start()
