# 3. найти повторы чисел

def repeat_dig(list_: list) -> dict:
    keys_ = set(list_)
    # dict_ = {}
    dict_ = dict.fromkeys(keys_, 0)
    for key in keys_:
        dict_[key] = list_.count(key)
        # print(dict_[key])
    return dict_


list_1 = [1, 1, 2, 3, 5, 8, 13, 21, 13, 2, 2, 21, 21, 21]
print(list_1)
print(repeat_dig(list_1))
