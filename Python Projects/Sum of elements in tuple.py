n = int(input())
l = []
for i in range(n):
    e = int(input())
    l.append(e)

t = tuple(l)

k = 0
s = 0
for j in range(len(t)):
    a = t[k]
    s = s+a
    k = k+1

print(s)