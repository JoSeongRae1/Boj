import sys
from collections import Counter

N = int(sys.stdin.readline())
A = [int(sys.stdin.readline()) for i in range(N)]
A.sort()

ans = [0, 0, 0, 0]

ans[0] = round(sum(A) / N)
ans[1] = A[(N-1)//2]

C = Counter(A).most_common()
if len(C) == 1:
    ans[2] = C[0][0]
else:
    ans[2] = C[1][0] if C[0][1] == C[1][1] else C[0][0]

ans[3] = A[N-1] - A[0]

for i in range(4):
    print(ans[i])