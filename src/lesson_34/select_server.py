import select
from socket import socket, AF_INET, SOCK_STREAM


def clients_read(r_clients: list, clientlist: list) -> dict:

    responses = {}

    for sock in r_clients:
        try:
            data = sock.recv(1024).decode('utf-8')
            if not data:
                print('No data')
                sock.close()
                clientlist.remove(sock)
            else:
                responses[sock] = data
        except OSError as e:
            print(e)
            sock.close()
            clientlist.remove(sock)

    return responses


def clients_write(requests: dict, w_clients: list, all_clients: list) -> None:
    for sock in w_clients:
        if sock in requests:
            try:
                response = requests[sock].encode('utf-8')
                sock.send(response.lower())
            except OSError as e:
                print(e)
                sock.close()
                all_clients.remove(sock)


def main_server():
    address = ('localhost', 8888)
    clients = []

    with socket() as sock:
        sock.bind(address)
        sock.listen(10)
        sock.setblocking(False)

        print('Server is RUN')

        while True:
            try:
                conn, addr = sock.accept()
                print(f'New connection from {addr}')
                conn.setblocking(False)
                clients.append(conn)
            except BlockingIOError as e:
                print(e)

            wait = 10
            r, w, e = select.select(clients, clients, [], wait)

            if r or w:
                requests = clients_read(r, clients)
                if requests:
                    clients_write(requests, w, clients)


if __name__ == '__main__':
    main_server()

