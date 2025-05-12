import random

secret_number = random.randint(1, 20)
debug_mode = False

print("I'm thinking of a number between 1 and 20.")
print("Type 'x' to exit the game at any time.")
print("Type 's' to show the secret number once (cheat).")
print("Type 'd' to toggle debug mode (shows secret number every turn).")

while True:
    if debug_mode:
        print(f"[DEBUG] Secret number: {secret_number}")
        
    guess = input("Take a guess: ")
    
    if guess.lower() == 'x':
        print("You chose to exit the game. Goodbye!")
        break
    elif guess.lower() == 's':
        print(f"(Cheat) The secret number is: {secret_number}")
        continue
    elif guess.lower() == 'd':
        debug_mode = not debug_mode
        print(f"Debug mode {'enabled' if debug_mode else 'disabled'}.")
        continue

    guess = int(guess)
    if guess < secret_number:
        print("Too low. Try again.")
    elif guess > secret_number:
        print("Too high. Try again.")
    else:
        print("You guessed the number!")
        break

