""" first variant

x = int(input())
sum_1 = 0
i = 1
for i in range(1, x + 1) :
    sum_1 = sum_1 + i ** 3
print(sum)

"""

#second variant
x = int(input())
sum_1 = 0
i = 1
while i <= x :
    sum_1 += i ** 3
    i += 1
print(sum_1)
