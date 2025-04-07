import numpy as np

r = float(input("Hi User, Please enter the radius of your choice: "))

area = np.pi * r ** 2
circum = 2 * np.pi * r

print(f"Area of the circle: {area:.2f}")
print(f"Circumference of the circle: {circum:.2f}")

