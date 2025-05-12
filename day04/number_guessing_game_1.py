import random

secret_number = random.randint(1, 20)
print("I'm thinking of a number between 1 and 20.")

while True:
    try:
        guess = int(input("Take a guess: "))
        if guess < secret_number:
            print("Try again.")
        elif guess > secret_number:
            print("Try again.")
        else:
            print("You guessed the number!")
            break

