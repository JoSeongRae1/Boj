N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

a, b, k = 0, 0, 0
while k < M:
    if A[a] < B[b]:
        a += 1
    else:
        A[a] -= B[b]
        b += 1
        k += 1

print(sum(A))