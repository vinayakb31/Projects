size = int(input('Enter size of array: '))
n = [int(input('Enter a value: ')) for _ in range(size)]
print('Original input is:', n)

s = len(n)
if s%2 != 0:
    s = s-1

for i in range(0, s, 2):
    n[i], n[i+1] = n[i+1], n[i]

print('The values after being swapped:', n)