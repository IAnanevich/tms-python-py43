n = 2
k = 2
list_f = [1, 1]
while n <= 15:
    list_f.append(k)
    k = list_f[n] + list_f[n - 1]
    n += 1
print(f' список чисел фиббоначи {list_f}')
