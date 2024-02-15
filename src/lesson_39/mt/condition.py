import threading

condition = threading.Condition()
shared_buffer = []
MAX_BUFFER_SIZE = 5


def producer():
    global shared_buffer
    for i in range(10):
        with condition:
            while len(shared_buffer) >= MAX_BUFFER_SIZE:
                condition.wait()
            shared_buffer.append(i)
            print(f'Produced: {i}')
            condition.notify()


def consumer():
    global shared_buffer
    for _ in range(10):
        with condition:
            while not shared_buffer:
                condition.wait()
            consumed_item = shared_buffer.pop(0)
            print(f'Consumed: {consumed_item}')
            condition.notify()


threading.Thread(target=producer).start()
threading.Thread(target=consumer).start()
