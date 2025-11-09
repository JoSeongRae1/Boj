
from collections import deque

N, M, V = map(int, input().split())
graph = {i: [] for i in range(1, N+1)}
for _ in range(M):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

dfs_nv = [V]
dfs_v = []
while dfs_nv:
    node = dfs_nv.pop()
    if node not in dfs_v:
        new = graph[node]
        new.sort(reverse=True)
        dfs_nv.extend(new)
        dfs_v.append(node)


bfs_nv = deque([V])
bfs_v = []
while bfs_nv:
    node = bfs_nv.popleft()
    if node not in bfs_v:
        new = graph[node]
        new.sort()
        bfs_nv.extend(new)
        bfs_v.append(node)

print(" ".join(map(str, dfs_v)))
print(" ".join(map(str, bfs_v)))