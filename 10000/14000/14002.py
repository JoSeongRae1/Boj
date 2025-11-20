N = int(input())
A = list(map(int, input().split()))
D = [1 for i in range(N)]
for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            D[i] = max(D[i], D[j]+1)

L = max(D)
ans = []
for i in range(N-1, -1, -1):
    if D[i] == L:
        ans.append(A[i])
        L -= 1
print(max(D))
print(*sorted(ans))