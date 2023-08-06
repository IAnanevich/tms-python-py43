# Сделать программу в которой нужно будет угадать число.

from random import randint

answer, tries = randint(1, 101), randint(7, 10)

while tries:
    number = int(input(f"You have {tries} tries(y), guess the number 1 to 100: "))
    tries -= 1
    if answer < number:
        print("Too much!")
    elif answer > number:
        print("Too few!")
    else:
        print(f"Correct! It was {answer}")
        break
else:
    print(f"You didn't guess! It was {answer}")
