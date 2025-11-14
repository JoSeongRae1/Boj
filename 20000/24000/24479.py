import sys

N, M, R = map(int, sys.stdin.readline().split())
graph = {i+1: [] for i in range(N)}
for i in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

nv = [R]
v = set()

k = 1
ans = {}
while nv:
    node = nv.pop()
    if node not in v:
        v.add(node)
        nv.extend(sorted(graph[node], reverse=True))
        ans[node] = k
        k += 1

for i in range(1, N+1):
    print(ans[i] if i in ans else 0)
        
        