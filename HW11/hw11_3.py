# Сделать функцию для фильтрации емейла (регуляркой)
import re


def check(email: str) -> bool:
    """
    Проверяет, корректно ли введен адрес почты
    :param email: адрес, который нужно проверить
    :return: Да/Нет - корректный ли емаил
    """
    expression = r"([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\"([]!#-[^-~ \t]|(\\[\t -~]))+\")@([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\[[\t -Z^-~]*])"
    pattern = re.compile(expression)
    if re.fullmatch(pattern=pattern, string=email):
        return True
    return False


print("me-email.com", check("me-email.com"))  # False
print("me-email@.com", check("me-email@.com"))  # False
print("me-email@google.com", check("me-email@google.com"))  # True
print("me-email@google@google.com", check("me-email@google@google.com"))  # False
