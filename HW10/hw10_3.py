# Сделать свое исключение и подключить его к try / except

class IntInputError(Exception):
    def __init__(self, message="Wrong input: value is not integer") -> None:
        # Инициализация класса с вызовом родительской инициализации
        self.message = message
        super().__init__(self.message)


a = input("Enter any number: ")

try:
    if not isinstance(a, int):
        raise IntInputError
except IntInputError as err:
    print(err)
finally:
    if not isinstance(a, int):
        a = 0
