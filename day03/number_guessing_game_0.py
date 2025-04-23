import random

computer_number = random.randint(1, 20)
guess = int(input("I'm thinking of a number between 1 and 20. Take a guess: "))
if guess < computer_number:
    print("Your guess is too low.")
elif guess > computer_number:
    print("Your guess is too high.")
else:
    print("Correct! You guessed it!")
