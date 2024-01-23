import socket
import time

sock = socket.socket()
sock.connect(('localhost', 9090))

messages = ['hello', 'world', 'how', 'are', 'you']

for message in messages:
    print(f'Отправка: {message}')
    sock.send(message.encode('utf-8'))
    time.sleep(1)
    data = sock.recv(1024)
    print(f'Получено: {data.decode("utf-8")}')
    print(30*'-')
