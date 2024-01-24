def my_generator(data):
    for elem in data:
        yield elem


gen = my_generator([1, 2, 3, 4, 5])
print(gen)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
