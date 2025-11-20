from itertools import *
N, M = map(int, input().split())
K = list(map(int, input().split()))
K.sort()
A = combinations_with_replacement(K, M)
A = list(set(A))
A.sort()
for i in A:
    print(*i)