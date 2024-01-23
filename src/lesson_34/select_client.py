from socket import socket


# messages = ['HELLO', 'WORLD', 'IT', 'IS', 'ME', 'HOW', 'ARE', 'YOU', 'I', 'BOT']


def client():
    with socket() as sock:
        try:
            sock.connect(('localhost', 8888))

            while True:
                message = input('Enter something: ')
                sock.send(message.encode('utf-8'))

                data = sock.recv(1024).decode('utf-8')
                if not data:
                    print('No data')
                    break

                print(f'Response: {data}')
        except Exception as e:
            print(e)


if __name__ == '__main__':
    client()
