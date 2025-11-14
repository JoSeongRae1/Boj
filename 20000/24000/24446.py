import sys
from collections import deque

N, M, R = map(int, sys.stdin.readline().split())
graph = {i+1: [] for i in range(N)}
for i in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

nv = deque([R])
v = set()
ans = {}
k = 1
ans[R] = 0
while nv:
    node = nv.popleft()
    if node not in v:
        v.add(node)
        k += 1
        S = graph[node]
        S.sort(reverse=True)
        for s in S:
            nv.append(s)
            if s not in ans:
                ans[s] = ans[node] + 1

for i in range(1, N+1):
    print(ans[i] if i in ans else -1)