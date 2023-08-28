# Два натуральных числа называют дружественными, если каждое из них равно
# сумме всех делителей другого, кроме самого этого числа. Найти все пары
# дружественных чисел, лежащих в диапазоне от 200 до 300.

def get_sum_divisors(number: int) -> int:
    """ Return the sum of the divisors of a number.

    :param number: the number to find the sum of the divisors
    :return: sum of the divisors
    """
    return sum(divisor for divisor in range(1, number) if not number % divisor)


def find_friendly_numbers(start: int = 200, end: int = 3000) -> dict:
    """ Return a dictionary of friendly numbers.

    :param start: start of the search
    :param end: end of search
    :return: the dictionary of friendly numbers
    """
    friendly_numbers = dict()
    checked = set()
    for number in range(start, end + 1):
        if number in checked:
            # don't clog up memory
            checked.remove(number)
            continue
        sum_divisors_of_number = get_sum_divisors(number)
        if number == sum_divisors_of_number or sum_divisors_of_number in checked:
            # don't check in vain
            continue
        elif sum_divisors_of_number > number:
            # remember checked
            checked.add(sum_divisors_of_number)
        sum_divisors_of_sum_divisor = get_sum_divisors(sum_divisors_of_number)
        if number == sum_divisors_of_sum_divisor:
            # EUREKA!!
            friendly_numbers[number] = sum_divisors_of_number
    return friendly_numbers


if __name__ == "__main__":
    for index, value in find_friendly_numbers().items():
        print(f"{index} friend {value}")
