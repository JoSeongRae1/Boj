import sys

N, M, R = map(int, sys.stdin.readline().split())
graph = {i+1: [] for i in range(N)}
for i in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

nv = [R]
v = set()

ans = {}
ans[R] = 0
while nv:
    node = nv.pop()
    if node not in v:
        v.add(node)
        S = sorted(graph[node])
        for s in S:
            if s not in v:
                ans[s] = ans[node] + 1
                nv.append(s)

for i in range(1, N+1):
    print(ans[i] if i in ans else -1)
        
        