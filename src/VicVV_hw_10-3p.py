# 3) преза.своё исключение


class FatalError(Exception):
    def __init__(self, *args):
        if args:
            self.ErrorText = args[0]
        else:
            self.ErrorText = None

    def __str__(self) -> str:
        # print('вызов __str__')
        if self.ErrorText:
            return f"{self.ErrorText}"
        else:
            return f"ошибка есть, а описания ошибки нет..."


def avg(x: float | str, y: float | str) -> float:
    try:
        z = pow(x * y, 0.5)
        return z
    except:
        raise FatalError("косяк с данными. это точно числа?") from None


print(f"1. {avg(3, 4)}")
# print(f'2. {avg(x=3, y="5" )}')
raise FatalError
