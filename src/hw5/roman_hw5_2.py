'''Написать программу для нахождения факториала.
Факториал натурального числа n определяется как
произведение всех натуральных чисел от 1 до n включительно .
Реализацию выполнить в виде рекурсивной функции.'''


def factorial(n: int) -> int:
    if n == 0:
        return 1
    return n * factorial(n - 1)


while True:
    number = input("Введите число: ")
    if number.isdigit():
        number = int(number)
        print(f'Факториал {number} равен: {factorial(number)}')
        break
    print('Введите целое число!')
