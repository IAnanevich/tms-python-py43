import sys
import os


def hello_print(target_name: str):
    print(f'Hello {target_name}')


def add_numbers(num_1, num_2):
    return num_1 + num_2


if len(sys.argv) != 3:
    with open("FAQ.txt", "r") as file:
        print(file.read())
else:
    try:
        num_1 = int(sys.argv[1])
        num_2 = int(sys.argv[2])
        result = add_numbers(num_1, num_2)
        print(f"Sum of {num_1} and {num_2} is: {result}")
    except ValueError:
        print("Please provide valid integers for addition.")

if __name__ == '__main__':
    add_numbers(os.getenv("env_num_1"), os.getenv("env_num_2"))