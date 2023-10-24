# *Сделать свое исключение и подключить к try/except


class MyError(Exception):
    """
    class MyError(parent of this class is Exception) with attribute and method
    Attributes: message
    Methods: __init__
    """
    def __init__(self, message: str) -> None:
        """
        Makes a new class object.
        :param message: message
        """
        self.message = message


"""
в чем разница?
self.message = message
super().__init__(message)
и
super().__init__(message)
self.message = message
"""
try:
    animal = input('Enter animal(not cat): ')
    if animal == 'cat':
        raise MyError('mya')
except Exception as error:
    print(error)
