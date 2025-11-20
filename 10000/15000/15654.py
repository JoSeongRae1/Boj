from itertools import *
N, M = map(int, input().split())
K = list(map(int, input().split()))
K.sort()
A = permutations(K, M)
for i in A:
    print(*i)