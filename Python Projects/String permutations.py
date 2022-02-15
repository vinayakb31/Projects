from itertools import permutations

s,k = input().split()
p = list(permutations(s,int(k)))
p = sorted(p, reverse=False)

for p in p:
    print(*p, sep='')