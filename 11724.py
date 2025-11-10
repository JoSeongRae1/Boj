N, M = map(int, input().split())
graph = {i: [] for i in range(N)}

for _ in range(M):
    u, v = map(int, input().split())
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)

ans = 1
nv = [0]
v = []

while nv:
    node = nv.pop()
    if node not in v:
        v.append(node)
        nv.extend(graph[node])

    if len(nv) == 0 and len(v) < N:
        for i in graph:
            if i not in v:
                nv.append(i)
                ans += 1
                break

print(ans)