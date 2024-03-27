import os


def hello_print(target_name: str):
    print(f'Hello {target_name}')


if __name__ == '__main__':
    hello_print(os.getenv("target_name"))