def count(dict_1):
    new_dict = {}
    for i in dict_1:
        new_dict[i] = new_dict.get(i, 0) + 1
    return new_dict


dict_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 8]
print(count(dict_1))
