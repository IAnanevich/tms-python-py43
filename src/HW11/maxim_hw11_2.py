# Сделать функцию для фильтрации емейла (регуляркой)
import re


def check_mail(mail: str) -> bool:
    """ EMail filtering.

    :param mail: email
    :return: True is correct, False isn't correct
    """
    if not isinstance(mail, str):
        raise TypeError("Parameter must be string")
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return True if re.match(pattern, mail) is not None else False


if __name__ == "__main__":
    print(check_mail("myname@gmail.com"))
    print(check_mail("myname"))
