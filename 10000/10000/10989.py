import sys

N = int(sys.stdin.readline())
M = {}
for i in range(N):
    k = int(sys.stdin.readline())
    if k not in M:
        M[k] = 0
    M[k] += 1


for i in range(1, 10001):
    if i in M:
        for j in range(M[i]):
            print(i)