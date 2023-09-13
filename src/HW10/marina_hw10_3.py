# Сделать свое исключение и подключить к трай эксепт


class StrHasNumberError(Exception):
    """
    class for my exception
    """

    def __init__(self, message: str) -> None:
        """
        :param message: message to display
        """
        self.message = message
        super().__init__(self.message)


def is_name(test_name: str) -> None:
    """
    check has the name numbers
    :param test_name: string for check
    :return: None
    """
    for st in test_name:
        # если символ - цифра, вызываем исключение
        if st in "0123456789":
            raise StrHasNumberError(f"Name '{test_name}' has numbers")
    # если цифр нет - сообщаем об этом
    print(f"'{test_name}' has any number")


# список для теста
name_list = ["Marina", "Mar3ina3", "25Marina"]
# проверка
for nam in name_list:
    try:
        is_name(nam)
    except StrHasNumberError as error:
        print(error)
# результат выполнения
# 'Marina' has any number
# Name 'Mar3ina3' has numbers
# Name '25Marina' has numbers
