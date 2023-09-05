class MyException(Exception):
    """
    Определяет пользовательское исключение MyException.
    """

    def __init__(self, message: str, code: int):
        """
        Инициализирует объект MyException.

        Аргументы:
        - message (str): Сообщение об ошибке.
        - code (int): Код ошибки.
        """
        self.message = message
        self.code = code

    def __str__(self) -> str:
        """
        Возвращает строковое представление исключения MyException.

        Возвращает:
        - str: Строковое представление исключения.
        """
        return f"MyException: {self.message} (Code: {self.code})"


try:
    raise MyException("Ошибка при работе с файлом", 404)
except MyException as e:
    print(e)
