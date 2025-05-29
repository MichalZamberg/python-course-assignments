import sys
from collections import Counter

def count_digits_in_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        return

    digit_counts = Counter(c for c in content if c.isdigit())

    with open('report.txt', 'w', encoding='utf-8') as report:
        for digit in map(str, range(10)):
            count = digit_counts.get(digit, 0)
            report.write(f"{digit} {count}\n")

    print("Digit counts written to 'report.txt'.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python count_digits_in_file.py <filename>")
    else:
        count_digits_in_file(sys.argv[1])
