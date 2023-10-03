import re

pattern = r'^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$'

mail1 = str(input('Enter email: '))


def checking_mail(mail: str) -> None:
    """

    :param mail: email
    :return: correct email
    """
    while re.search(pattern=pattern, string=mail):
        print(f'correct email: {mail}')
        break
    else:
        print(f'incorrect email: {mail}')
        checking_mail(str(input('try again: ')))


print(checking_mail(mail1))
