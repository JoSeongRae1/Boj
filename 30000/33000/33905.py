N, M, K = map(int, input().split())
graph = {i: [] for i in range(1, N+2)}
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
L = list(map(int, input().split()))

nv = [1]
v = []
while nv:
    node = nv.pop()
    if node not in v and node not in L:
        v.append(node)
        nv.extend(graph[node])
print(len(v) - 1)