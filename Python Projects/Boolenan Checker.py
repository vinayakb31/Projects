def isPalindrome(x):
    return x == x[::-1]

x = input()
y = isPalindrome(x)

if y:
    print('true')
else:
    print('false')
