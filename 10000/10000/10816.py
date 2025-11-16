N = int(input())
A = input().split()
d = {}
for v in A:
    if v not in d:
        d[v] = 0
    d[v] += 1
M = int(input())
B = input().split()
for v in B:
    print(d[v] if v in d else 0, end=' ')