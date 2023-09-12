# Сделать функцию для фильтрации e-mail
import re


def fil(string: str) -> str:
    """
    Checks e-mail
    :param string: string
    :return: 'Good e-mail' or 'Not e-mail'
    """
    if re.fullmatch(pattern=r'\w+@[a-z]*\.[a-z]*', string=string):
        return 'Good e-mail'
    return 'Not e-mail'
