# Сделать свое исключение и подключить к try/except.

class IsInvalidInput(Exception):
    """ My exception """
    def __init__(self, message="Invalid input") -> None:
        self.message = message
        super().__init__(self.message)


if __name__ == "__main__":
    try:
        if True:
            raise IsInvalidInput
    except IsInvalidInput as error:
        print(error)
