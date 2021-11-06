def gcd(x, y):
    while(y):
        x, y = y, x%y
    return x
def lcm(x, y):
    lcm = (x*y)//gcd(x, y)
    return lcm
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
print("The LCM is", lcm(num1, num2))
print("The GCD is", gcd(num1, num2))