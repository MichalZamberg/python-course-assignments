import sys
from collections import Counter

def count_words(input_path, output_path):
    with open(input_path, 'r') as file:
        text = file.read().lower()

    words = text.split()
    word_counts = Counter(words)

    sorted_words = sorted(word_counts.items())
    max_word_length = max(len(word) for word, _ in sorted_words)

    with open(output_path, 'w') as file:
        for word, count in sorted_words:
            file.write(f"{word.ljust(max_word_length + 1)}{count}\n")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python count_words_from_a_file.py <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    count_words(input_file, output_file)
