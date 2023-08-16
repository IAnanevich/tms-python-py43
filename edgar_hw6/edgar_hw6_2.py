# Написать лямбда-функцию определяющую четное\нечетное. Функция принимает параметр (число) и если четное, то
# выдает слово "четное", если ет - то "нечетное"
# -------------------------------------------------------------------------------------------------------------

check_even_or_odd = lambda x: "odd" if x % 2 else "even"

# Example

while True:
    try:
        num = int(input("Enter num: "))
        print(f'Number {num} - {check_even_or_odd(num)}')
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")
