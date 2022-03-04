# Sphere calculator

from cmath import pi

r = int(input('Enter the radius of the sphere'))

print("""
What do you want to calculate?
1. Surface Area
2. Volume

""")
f = int(input('Enter the number'))

if f == 1:
    res = 4*pi*r**2
elif f == 2:
    res = (4/3)*pi*r**3

format_res = "{:.2f}".format(res)

if f == 1:
    n = 'surface area'
elif f == 2:
    n = 'volume'

print('The', n, 'of the sphere is:', format_res)
