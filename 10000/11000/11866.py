from collections import deque

N, K = map(int, input().split())
D = deque(range(1, N+1))
ans = []
while len(D) > 0:
    for i in range(K-1):
        D.append(D.popleft())
    ans.append(D.popleft())
print('<', ", ".join(map(str, ans)), '>', sep='')