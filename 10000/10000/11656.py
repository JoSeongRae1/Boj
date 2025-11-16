S = input()
N = len(S)
A = []
for i in range(N):
    A.append(S[i:N+1])
A.sort()
for v in A:
    print(v) 