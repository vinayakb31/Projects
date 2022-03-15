l = eval(input('Enter list with brackets and commas: '))
l1 = []
for i in l:
    if i%2 == 0:
        a = i/2
    else:
        a = i*2
    l1.append(a)
print(l1)
