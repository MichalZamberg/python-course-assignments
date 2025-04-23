import sys
import numpy as np

if len(sys.argv) != 3:
    print("Usage: python rectangle_calculations.py <height> <width>")
    sys.exit(1)

h = float(sys.argv[1])
w = float(sys.argv[2])

area = h * w
perimeter = 2 * (h + w)

print(f"The area of the rectangle: {area:.2f}")
print(f"The perimeter of the rectangle: {perimeter:.2f}")
