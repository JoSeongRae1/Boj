N = int(input())
A = list(map(int, input().split()))
D = [1 for i in range(N)]
for i in range(N):
    for j in range(i):
        if A[i] < A[j]:
            D[i] = max(D[i], D[j]+1)

print(max(D))