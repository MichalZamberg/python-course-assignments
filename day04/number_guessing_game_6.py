import random


secret_number = random.randint(1, 20)
debug_mode = False
move_mode = False

print("I'm thinking of a number between 1 and 20.")
print("Commands:")
print("  'x' to exit the game")
print("  'n' to start a new game")
print("  's' to show the secret number once (cheat)")
print("  'd' to toggle debug mode (always show secret)")
print("  'm' to toggle move mode (secret number shifts each turn)")

while True:
    if debug_mode:
        print(f"[DEBUG] Secret number: {secret_number}")
        
    guess = input("Take a guess: ")
    
    if guess.lower() == 'x':
        print("You chose to exit the game. Goodbye!")
        break
    elif guess.lower() == 'n':
        secret_number = random.randint(1, 20)
        print("Starting a new game. A new number has been chosen.")
        continue
    elif guess.lower() == 's':
        print(f"(Cheat) The secret number is: {secret_number}")
        continue
    elif guess.lower() == 'd':
        debug_mode = not debug_mode
        print(f"Debug mode {'enabled' if debug_mode else 'disabled'}.")
        continue
    elif guess.lower() == 'm':
        move_mode = not move_mode
        print(f"Move mode {'enabled' if move_mode else 'disabled'}.")
        continue


    guess = int(guess)
    if guess < secret_number:
        print("Too low. Try again.")
    elif guess > secret_number:
        print("Too high. Try again.")
    else:
        print("Congratulations! You guessed the number.")
        secret_number = generate_secret()
        print("Starting a new game. A new number has been chosen.")
        continue


    if move_mode:
        shift = random.randint(-2, 2)
        secret_number += shift
        secret_number = max(1, min(secret_number, 100))
