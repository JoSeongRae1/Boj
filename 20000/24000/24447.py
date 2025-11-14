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
d = {}
k = 1
d[R] = 0
t = {}
while nv:
    node = nv.popleft()
    if node not in v:
        v.add(node)
        t[node] = k
        k += 1
        S = graph[node]
        S.sort(reverse=True)
        for s in S:
            nv.append(s)
            if s not in d:
                d[s] = d[node] + 1

ans = 0
for i in range(1, N+1):
    a = d[i] if i in d else -1
    b = t[i] if i in t else 0
    ans += a * b
print(ans)