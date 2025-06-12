import sys
from digit_counter import count_digits, write_report

def count_digits_in_file(filepath):
    """Read file content, count digits, and write a report."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        return

    digit_counts = count_digits(content)
    write_report(digit_counts)
    print("Digit counts written to 'report.txt'.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python count_digits_main.py <filename>")
    else:
        count_digits_in_file(sys.argv[1])
