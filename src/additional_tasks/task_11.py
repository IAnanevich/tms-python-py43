# Создать lambda функцию, которая принимает на вход неопределенное количество именных аргументов
# и выводит словарь с ключами удвоенной длины. {‘abc’: 5} -> {‘abcabc’: 5}
# (тут обратите внимание, что в качестве аргументов лямбды можно также использовать *args и **kwargs)


new_dict = lambda **variables: {
    f"{key}{key}": value for key, value in variables.items()
}
# выводим результат применения функции
print(new_dict(a=5, b={1, 2}, dama=[3, 7, "t"]))
