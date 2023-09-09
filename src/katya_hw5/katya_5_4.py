from datetime import datetime, timedelta

# Сделать функцию, которая будет вызываться из генератора списков
# и по запросу к ней отдавать текущее время с задержкой в секунду. количество элементов
# нового списка запрашивать у пользователя


def return_time(i: int) -> str:
    """
    Return the time increased by 1 second
    :param i: number of elements
    :return: time in the specified format
    """
    return datetime.strftime(datetime.now() + timedelta(seconds=+i), "%Y-%m-%d %H:%M:%S")


number_of_items = int(input("Введите количесво элементов: "))

dict_date = []
for i in range(number_of_items):
    dict_date.append(return_time(i))
print(dict_date)
