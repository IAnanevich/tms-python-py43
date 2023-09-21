# Сделать функцию для фильтрации емейла (регуляркой)
import re


def filter_emails(email):
    """
    :param email: input text (str)
    :return: pattern (matches) find (email)
    """
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    matches = re.findall(pattern, email)
    return matches


try:
    text = input("Enter email-adress: ")
    email_list = filter_emails(text)

    if email_list:
        print("Find is email-adress: ")
        for _ in email_list:
            print(_)
    else:
        print("Email is not find")
except KeyboardInterrupt:
    print("Enter is failed")
except Exception as e:
    print(f"Error: {e}")
