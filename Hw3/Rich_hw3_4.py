num = int(input("Введите целое число"))
a = 0
i = 1
while i <= num:
    a += i ** 3
    i += 1
print(a)

####################################################

num = int(input("Введите целое число "))
a = 0
for i in range(1, num + 1):
     a += i ** 3
print(a)

