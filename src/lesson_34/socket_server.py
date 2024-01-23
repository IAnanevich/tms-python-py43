import socket
import time

sock = socket.socket()
sock.bind(('localhost', 9090))
sock.listen(1)


print('Сервер запущен')
conn, addr = sock.accept()
print(f'Адрес клиента {addr}')


while True:
    data = conn.recv(1024)

    if not data:
        break

    print(f'Получено о клиента: {data.decode("utf-8")}')

    conn.send(data.upper())
    time.sleep(1)
    print(f'Отправлено клиенту: {data.upper()}')
    print(30*'-')


conn.close()
