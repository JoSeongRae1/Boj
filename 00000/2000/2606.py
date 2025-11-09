N = int(input())
graph = {i: [] for i in range(1, N+1)}

K = int(input())
for _ in range(K):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)


nv = [1]
v = []
while nv:
    node = nv.pop()
    if node not in v:
        nv.extend(graph[node])
        v.append(node)

print(len(v)-1)