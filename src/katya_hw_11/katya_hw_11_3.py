import re

pattern = r"^[a-zA-z0-9!#%&*+-/=?^_{|}]+[^./b]+@[a-zA-z0-9-]+[^-/b]+\.[a-zA-z0-9-][^-/b]+$"


def mail(email: str) -> None:
    """
    Filter email
    :param email: Email
    :return: None
    """
    if isinstance(email, str) and re.match(pattern, email) is not None:
        print(f"Проверка пройдена - {email}")
    else:
        print(f"Проверка не пройдена - {email}")


mail("makarenkoek.@yandex.ru")
mail("makarenkoek@yandex.ru")
mail("makarenkoek@yandex-.ru")
mail("hhhh")
mail(1)
