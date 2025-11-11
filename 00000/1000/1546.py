N = int(input())
A = list(map(int, input().split()))
M = max(A)
S = []
for i in A:
    S.append(i/M*100)
print(sum(S)/N)