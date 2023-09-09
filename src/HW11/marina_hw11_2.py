# Сделать функцию для фильтрации email (регуляркой).
import re


def check_email(email: str) -> None:
    """
    check string if it is an email
    :param email: string for check
    :return: none
    """
    # pat = r'\w+@\w+\.\w+'
    pat = r"^([a-zA-z0-9_]+)(\.?)([a-zA-z0-9_]+)@(([^\b-])([a-zA-z0-9-]+)([^-\b])){,63}\.(([a-zA-z0-9]+)){,63}+$"
    if re.fullmatch(pat, email) is not None:
        print("is an email")
    else:
        print("NOT")


# проверка
check_email("mar3i@-mail.ru")  # NOT
check_email("ma______ri@mail.ru")  # is an email
check_email("ma..ri@mail.ru")  # NOT
check_email(".mari@mail.ru")  # NOT
check_email("mari.@mail.ru")  # NOT
check_email("ma.ri@mail.ru")  # is an email
