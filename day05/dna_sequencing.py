import sys

if len(sys.argv) != 2:
    print("Usage: python dna_sequencing.py <sequence>")
    sys.exit(1)

input_sequence = sys.argv[1].upper()
parts = input_sequence.split('X')
valid_sequences = [part for part in parts if set(part).issubset({'A', 'C', 'T', 'G'}) and part != '']
sorted_sequences = sorted(valid_sequences, key=len, reverse=True)

print(sorted_sequences)
