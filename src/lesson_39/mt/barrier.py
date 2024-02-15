import threading

barrier = threading.Barrier(3)


def worker():
    print("Thread is ready")
    barrier.wait()
    print("Thread continues execution")


threading.Thread(target=worker).start()
threading.Thread(target=worker).start()
threading.Thread(target=worker).start()
