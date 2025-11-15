n = int(input())
A = [[0] + list(map(int, input().split())) + [0] for i in range(n)]

for i in range(1, n):
    for j in range(1, i+2):
        A[i][j] = max(max(A[i-1][j-1], A[i-1][j]) + A[i][j], A[i][j])

print(max(A[n-1]))