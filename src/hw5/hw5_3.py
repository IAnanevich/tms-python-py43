# сколько раз встречается числа в списке
list_numbers = [1,3,5,2,2,3,4,2,3,1,4,1]

list_sum = {}
for number in list_numbers:
    if list_sum.get(number) is None:
        list_sum[number] = list_numbers.count(number)

print(list_sum)
