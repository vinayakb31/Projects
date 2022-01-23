# Hypotenuse calculator

import math

p = int(input('Enter the height of the triange: '))
b = int(input('Enter the base length of the triangle: '))
h = math.sqrt(p**2 + b**2)
print(h)