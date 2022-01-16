# Taking user inputs
size = int(input('Enter the size of the list: '))
n = [int(input('Enter a value: ')) for _ in range(size)]

print('Original input:', n)

a = max(n)
b = min(n)
print('The largest number in the list:', a)
print('The smallest number in the list:', b)
