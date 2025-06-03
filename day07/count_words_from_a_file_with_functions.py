from collections import Counter

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read().lower()

def count_words(text):
    return Counter(text.split())

def write_word_counts(word_counts, output_path):
    sorted_words = sorted(word_counts.items())
    max_word_len = max(len(word) for word, _ in sorted_words)
    with open(output_path, 'w') as f:
        for word, count in sorted_words:
            f.write(f"{word.ljust(max_word_len + 1)}{count}\n")

def main(input_path, output_path):
    text = read_file(input_path)
    word_counts = count_words(text)
    write_word_counts(word_counts, output_path)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python count_words_from_a_file_with_functions.py <input> <output>")
        sys.exit(1)
    main(sys.argv[1], sys.argv[2])
