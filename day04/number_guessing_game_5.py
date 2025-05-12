import random

secret_number = random.randint(1, 20)
debug_mode = False
move_mode = False

print("I'm thinking of a number between 1 and 20.")
print("Commands:")
print("  'x' to exit the game")
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

    try:
        guess = int(guess)
        if guess < secret_number:
            print("Try again.")
        elif guess > secret_number:
            print("Try again.")
        else:
            print("You guessed the number!")
            break
    except ValueError:
        print("Please enter a valid number, or one of the commands: 'x', 's', 'd', or 'm'.")
        continue

    if move_mode:
        shift = random.randint(-2, 2)
        secret_number += shift
        # Keep secret_number in 1–20 range
        secret_number = max(1, min(secret_number, 20))
