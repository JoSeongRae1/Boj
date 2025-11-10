N, M = map(int, input().split())

A = set([input() for _ in range(N)])
B = set([input() for _ in range(M)])
S = list(A & B)
S.sort()

print(len(S))
for i in S:
    print(i)