from itertools import *
N, M = map(int, input().split())
A = combinations_with_replacement(range(1, N+1), M)
for i in A:
    print(*i)