# Сделать свое исключение и подключить к try/except.
from datetime import datetime


# deadline = datetime.strptime("22/05/2017", "%d/%m/%Y")

class IsInvalidDate(Exception):
    """ My exception """
    def __init__(self, message="Invalid date format") -> None:
        self.message = message
        super().__init__(self.message)


if __name__ == "__main__":
    try:
        d, m, y = '20-09-2020T'.split('-')
        if not (d.isdigit() and m.isdigit() and y.isdigit()):
            raise IsInvalidDate
    except Exception as error:
        print(error)
