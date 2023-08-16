even = lambda num: "четное" if num % 2 == 0 else "нечетное"
try:
    number = int(input("Введите число: "))
except ValueError:
    print("Note find number")
else:
    result = even(number)
    print(f"Число: {number} является: {result}")
