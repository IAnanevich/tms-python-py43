# Для каждого натурального числа в промежутке от m до n вывести все делители,
# кроме единицы и самого числа, m и n вводятся с клавиатуры


def find_divisors(numb: int) -> list[int]:
    """
    print list of divisors without 1 and number
    :param numb: a number which divisors we find
    :return: list of divisors
    """
    div_list = []

    for j in range(1, numb // 2 + 1):
        if not numb % j:
            div_list.append(j)
    return div_list[1::]


while True:
    m = input("Enter integer number start of interval: ")
    n = input("Enter integer number end of interval: ")
    if m.isdigit() and n.isdigit():
        for i in range(int(m), int(n) + 1):
            print(f"Divisors of number {i}(except 1 and {i}) : {find_divisors(i)}")
        break
    print("You need to enter two INTEGER number. Try again")
