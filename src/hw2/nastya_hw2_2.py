# Дан произвольный список. Представьте его в обратном порядке. ([1, 2, 3] -> [3, 2, 1]

i = int(input('Enter the number of values is in the list: '))
j = []
for b in range(i):
    x = input('Enter a value into the list: ')
    j.append(x)
print(j)
print(j[::-1])

#####################################################################################

print([1, 2, 3][::-1])
