# Сделать программу в которой нужно будет угадывать число

from random import randint

number = randint(1, 100)
# print(number)  # чтобы знать. что угадать)

while True:
    guess_number = int(input('Please, guess target number (from 1 to 100): '))
    if guess_number > number:
        print(f'Your number {guess_number} is bigger than target, try again :)')
    elif guess_number < number:
        print(f'Your number {guess_number} is less than target, try again :)')
    else:
        print(f'!Congratulations! \nYour number {guess_number} is right :)')
        break
