N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = M
for i in range(M):
    if A[i] in B:
        ans -= 1

print(ans)