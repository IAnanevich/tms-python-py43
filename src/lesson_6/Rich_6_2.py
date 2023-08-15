Chetka = lambda num: "четное" if num % 2 == 0 else "нечетное"

number = int(input("Введите число: "))
result = Chetka(number)
print(f"Число: {number} является: {result}")
