import random

secret_number = random.randint(1, 100)
print("I'm thinking of a number between 1 and 100.")
print("Type 'x' to exit the game at any time.")

while True:
    guess = input("Take a guess: ")
    if guess.lower() == 'x':
        print("You chose to exit the game. Goodbye!")
        break
    try:
        guess = int(guess)
        if guess < secret_number:
            print("Try again.")
        elif guess > secret_number:
            print("Try again.")
        else:
            print("You guessed the number!")
            break

