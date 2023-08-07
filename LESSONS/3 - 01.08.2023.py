spam_1 = 'spam_1'
spam_2, spam_3 = 'spam_2', 'spam_3'
print(spam_1, spam_2, spam_3)
# spam_1 spam_2 spam_3

[spam_4, spam_5] = ['spam_4', 'spam_5']
print(spam_4, spam_5)
# spam_4 spam_5

[spam_6, spam_7] = ['spam_61', 'spam_62'], ['spam_71', 'spam_72']
print(spam_6, spam_7)
# ['spam_61', 'spam_62'] ['spam_71', 'spam_72']

a, b, c, d = 'spam'
print(a, b, c, d)
# s p a m

x, *y = 'spam'
print(x, y)
# s ['p', 'a', 'm']

# ============
firstname = "Alex"
lastname = "Klen"
print("Hello, {} {}".format(firstname, lastname))
print("Hello, {0} {1}".format(firstname, lastname))
print(f'Hello, {firstname} {lastname}')
# Hello, Alex Klen


# ============
a = 11
if a > 5:
    a += 5
    if a > 10:
        a += 10
print(f'\na = {a}')

# ============
age = 18
is_more_then_17 = True if age > 17 else False
print(f'\n age is {age}, its more then 17? = {is_more_then_17}')

# ============
print('\n')
for i in range(1, 10, 1):
    print(i)

# ============
print('\n')
for e in [1, 3, 5, 7]:
    print(e)

# ============
print('\n')
for e in [1, 2]:
    print(e)
    if e == 3:
        break
else:
    print("Не выполняется, если выполнился break")

# ============
print('\n')
a = [1, 2, 3, 4]
for index, value in enumerate(a):
    print(f" id is {index}, value is {value}")

# ============
print('\n')
a = [1, 2, 3]
b = [5, 6, 7, 8, 9, 10]
c = zip(a, b)
print(list(c))
