import re

# Prompt user to enter a sequence via standard input
input_sequence = input("Please type in a sequence: ").upper()

# Find all contiguous sequences of A, C, T, G
valid_sequences = re.findall(r'[ACTG]+', input_sequence)

# Sort the sequences by length in descending order
sorted_sequences = sorted(valid_sequences, key=len, reverse=True)

print(sorted_sequences)
