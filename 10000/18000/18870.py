N = int(input())

X = list(map(int, input().split()))
S = list(set(X))
M = {}

S.sort()

ind = 0
for v in S:
    M[v] = ind
    ind += 1

for i in X:
    print(M[i], end=" ")