import random


def guess_the_number():
    secret_number = random.randint(1, 100)

    attempts = 0
    max_attempts: int = 5

    while attempts < max_attempts:

        guess = int(input("Enter int 1 to 100: "))

        if guess == secret_number:
            print("Congrats! You guessed the number")
            break
        elif guess < secret_number:
            print("No, the mystery number is bigger: ")
        else:
            print("No, the mystery number is smaller: ")

        attempts += 1
    if attempts == max_attempts:
        print(f"You're out of tries. The number you guessed was: {secret_number}")


guess_the_number()

