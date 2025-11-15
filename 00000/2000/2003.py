N, M = map(int, input().split())
A = list(map(int, input().split()))
S = [0]
for i in range(N):
    S.append(A[i] + S[i])

ans = 0
for i in range(N+1):
    for j in range(i+1, N+1):
        if S[j] - S[i] == M:
            ans += 1

print(ans)