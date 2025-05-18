numbers = [1203, 1256, 312456, 98]

digit_counts = {str(d): 0 for d in range(10)}

for number in numbers:
    for digit in str(number):
        digit_counts[digit] += 1

for digit in range(10):
    print(f"{digit}  {digit_counts[str(digit)]}")
