import random

secret_number = random.randint(1, 20)
print("I'm thinking of a number between 1 and 20.")
print("Type 'x' to exit the game at any time.")
print("Type 's' to reveal the secret number (cheat).")

while True:
    guess = input("Take a guess: ")
    if guess.lower() == 'x':
        print("You chose to exit the game. Goodbye!")
        break
    elif guess.lower() == 's':
        print(f"(Cheat) The secret number is: {secret_number}")
        continue
        
    guess = int(guess)
    if guess < secret_number:
        print("Too low. Try again.")
    elif guess > secret_number:
        print("Too high. Try again.")
    else:
        print("You guessed the number!")
        break

