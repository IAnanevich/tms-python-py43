# Для каждого натурального числа в промежутке от m до n вывести все делители,
# кроме единицы и самого числа. m и n вводятся с клавиатуры.

def get_divisors(number: int) -> list:
    """ Return the divisors of a number

    :param number: the number to find the divisors
    :return: list of the divisors
    """
    return [divisor for divisor in range(2, number) if not number % divisor]


def numbers_divisors(start: int, end: int) -> dict:
    """ Return dictionary where key is number from the range and value the divisors of a number.

    :param start: start of the range
    :param end: end of the range
    :return: dictionary of numbers with divisors
    """
    return {i: get_divisors(i) for i in range(start, end + 1)}


if __name__ == "__main__":
    start_range, end_range = input("Enter the start range: "), input("Enter the end range: ")
    try:
        start_range, end_range = int(start_range), int(end_range)
    except TypeError as error:
        print(error)
    print(numbers_divisors(start_range, end_range))
