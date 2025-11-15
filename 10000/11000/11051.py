import sys

N, K = map(int, sys.stdin.readline().split())
ans = 1
for i in range(K):
  ans *= (N-i)
  ans //= (i+1)

print(int(ans) % 10007)