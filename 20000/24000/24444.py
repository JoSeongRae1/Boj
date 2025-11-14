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
while nv:
    node = nv.popleft()
    if node not in v:
        v.add(node)
        ans[node] = k
        k += 1
        S = graph[node]
        S.sort()
        for s in S:
            nv.append(s)

for i in range(1, N+1):
    print(ans[i] if i in ans else 0)