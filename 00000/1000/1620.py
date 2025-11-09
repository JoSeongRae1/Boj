N, M = map(int, input().split())
A = {}
B = {}
for i in range(N):
    s = input()
    A[i] = s
    B[s] = i

for i in range(M):
    s = input()
    if s.isdigit():
        s = int(s)
        print(A[s-1])
    else:
        print(B[s]+1)