import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
G = {}
for i in range(N):
    A, B = sys.stdin.readline().rstrip().split()
    G[A] = B
for i in range(M):
    A = sys.stdin.readline().rstrip()
    print(G[A])   