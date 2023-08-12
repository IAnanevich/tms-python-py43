def count(numbers_list):
    list = {}
    for number in numbers_list:
        if list.get(number) is not None:
            list[number] += 1
        else:
            list[number] = 1
    return list


numbers = [5,5,5,5,5,1,1,1,12,2,2]
result = count(numbers)
for number, count in result.items():
    print(f"Число {number} встречается {count} раз")
