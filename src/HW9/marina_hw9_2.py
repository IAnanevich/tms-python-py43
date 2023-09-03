# Реализовать любой мета класс (сами придумываете что ваш класс будет делать)
# Переименовывает все методы класса в funk_n, где n - порядковый номер метода в описании
from typing import Callable, Any


class MyMeta(type):
    """
    Переименовывает все методы класса в funk_n, где n - порядковый номер метода в классе
    """

    def __new__(cls, name: str, bases: tuple[Any], attrs: dict[Any, Any]) -> Any:
        """
        constructor
        :param name: name
        :param bases: bases
        :param attrs: attrs
        """
        at = {}  # словарь на подмену
        ind = 1  # порядковый номер метода в классе
        for key, value in attrs.items():
            if callable(value):
                at[f"funk_{ind}"] = value
                ind += 1
                continue
            at[key] = value
        return super().__new__(cls, name, bases, at)


class Messages(metaclass=MyMeta):
    """
    Класс с двумя методами
    """

    @staticmethod
    def get_hello_world() -> None:
        """
        text Hello World
        :return: None
        """
        print("Hello world")

    @staticmethod
    def get_winter() -> None:
        """
        text Winter is coming
        :return: None
        """
        print("Winter is coming")


# проверка с новыми названиями методов
my_text = Messages()
# ниже - ругается на метод, поэтому уношу в игнор
my_text.funk_1()  # type: ignore
my_text.funk_2()  # type: ignore
