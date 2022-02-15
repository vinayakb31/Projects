n = int(input())
a = input().split()
a = tuple(map(int,a))
print(hash(a))