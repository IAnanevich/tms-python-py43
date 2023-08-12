def plus(a, b):
    return a + b


def minus(a, b):
    return a - b


def mult(a, b):
    return a * b


def div(a, b):
    return a / b


def exp(a, b):
    return a ** b


while True:
    a = int(input())
    b = int(input())
    print("1.Сложение")
    print("2.вычитание")
    print("3.умножение")
    print("4.деление")
    print("5.возведение в степень")
    print('6.выход')
    choice = int(input('Выберете число '))


    if choice == 1:
        c = plus(a,b)
        print(c)
    elif choice == 2:
        c = minus(a,b)
        print(c)
    elif choice == 3:
        c = mult(a,b)
        print(c)
    elif choice == 4:
        c = div(a,b)
        print(c)
    elif choice == 5:
        c = exp(a,b)
        print(c)
    elif choice == 6:
        break
    else:
        print("Выберете чилсо от 1 до 5")
