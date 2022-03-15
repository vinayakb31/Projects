n = int(input())
l = []
l1 = []
k = 0
for i in range(n):
    e = int(input())
    l.append(e)

print(l)
for i in range(n):
    if l[k]%2==0:
        a = l[k]/2
    else:
        a = l[k]*2
    l1.append(a)
    k = k+1

print(l1)