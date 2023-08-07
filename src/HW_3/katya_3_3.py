# Дан список целых чисел. подсчиать сколько четных чисел в списке

spisok_1 = [2, 6, 56, 87, -3, 99,]
n1 = 0
n2 = 0

# n = 0
# while n < len(spisok_1):
#     if bool(spisok_1[n]%2) == False:
#         n1 += 1
#         n += 1
#     elif bool(spisok_1[n]%2) == True:
#         n2 += 1
#         n += 1
# else:
#     print(f'Количество четных чисел {n1}, количество нечетных чисел {n2}')

for i in spisok_1:
    if bool(i % 2) == False:
        n1 += 1
        i += 1
    else:
        n2 = len(spisok_1)-n1
print(f'Количество четных чисел {n1}, количество нечетных чисел {n2}')