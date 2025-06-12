from collections import Counter

def count_digits(content):
    """Count the occurrences of each digit in the given string content."""
    return Counter(c for c in content if c.isdigit())

def write_report(digit_counts, output_path='report.txt'):
    """Write digit counts to a report file."""
    with open(output_path, 'w', encoding='utf-8') as report:
        for digit in map(str, range(10)):
            count = digit_counts.get(digit, 0)
            report.write(f"{digit} {count}\n")
