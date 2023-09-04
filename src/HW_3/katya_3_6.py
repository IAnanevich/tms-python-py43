# n = 2
# k = 2
# list_f = [1, 1]
#
# while n <= 15:
#     list_f.append(k)
#     k = list_f[n] + list_f[n - 1]
#     n += 1
# print(f' список чисел фибоначчи {list_f}')

list_f = [1, 1]
for n in range(1, 15):
    k = list_f[n] + list_f[n - 1]
    list_f.append(k)

print(f' список чисел фибоначчи {list_f}')
