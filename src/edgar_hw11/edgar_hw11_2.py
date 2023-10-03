import re


def filter_emails(emails):
    """
    Фильтрует email-адреса из списка строк.

    :param emails: Список строк для фильтрации.
    :return: Список корректных email-адресов.
    """
    valid_emails = []
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

    for email in emails:
        if re.match(email_pattern, email):
            valid_emails.append(email)

    return valid_emails


# Пример использования функции
input_emails = ["user@example.com", "invalid-email", "another@example.com", "123@abc.xyz"]
valid_emails = filter_emails(input_emails)
print(valid_emails)
