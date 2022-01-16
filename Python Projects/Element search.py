# Taking user inputs 
size = int(input('Enter the number of elements you want to input: '))
n = [(input('Enter a value: ')) for _ in range(size)]

print('Original input:', n) 

# The term the user wants to search for
x = input('Enter the element that you want to search for: ')

if x in n:
    print(x, 'found!')
else:
    print(x, 'not found!')
