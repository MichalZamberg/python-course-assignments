import sys
import numpy as np

if len(sys.argv) != 2:
    print("Usage: python circle_calculations.py <radius>")
    sys.exit(1)

r = float(sys.argv[1])

area = np.pi * r ** 2
circum = 2 * np.pi * r

print(f"Area of the circle: {area:.2f}")
print(f"Circumference of the circle: {circum:.2f}")
