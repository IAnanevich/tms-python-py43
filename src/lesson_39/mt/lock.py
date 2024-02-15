import threading

shared_data = 0
lock = threading.Lock()


def update_shared_data():
    global shared_data
    with lock:
        print(shared_data)
        shared_data += 1
        # if shared_data == 5:
        #     lock.acquire()


threads = [threading.Thread(target=update_shared_data) for _ in range(10)]

for thread in threads:
    thread.start()


for thread in threads:
    thread.join()


print(shared_data)
