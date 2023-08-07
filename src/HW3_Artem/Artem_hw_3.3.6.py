#Составить список чисел Фибоначчи содержащий 15 элементов.
a = b = 1
n = int(input())

print(a)
print(b)
for i in range(2, n):
    a, b = b, a + b
    print(b)




