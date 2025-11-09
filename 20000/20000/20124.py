A = []
for _ in range(int(input())):
    N, S = input().split()
    A.append((N, int(S)))
A.sort(key=lambda x: (-x[1], x[0]))
print(A[0][0])