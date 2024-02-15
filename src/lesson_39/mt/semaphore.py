import threading
from time import sleep

semaphore = threading.Semaphore(value=10)


def access_database():
    with semaphore:
        print('Accessing to database')
        sleep(3)

#  utl/page=1,2,3,4...1000


for _ in range(1000):
    threading.Thread(target=access_database).start()
