from collections import deque

M, N, H = map(int, input().split())
graph = []

for i in range(H):
    graph.append([list(map(int, input().split())) for j in range(N)])

d = [(0, 0, 1), (0, 1, 0), (1, 0, 0), (0, 0, -1), (0, -1, 0), (-1, 0, 0)]
nv = deque()
for i in range(H):
    for j in range(N):
        for k in range(M):
            if graph[i][j][k] == 1:
                nv.append((i, j, k))

while nv:
    x, y, z = nv.popleft()
    for dx, dy, dz in d:
        if 0 <= x+dx < H and 0 <= y+dy < N and 0 <= z+dz < M:
            if graph[x+dx][y+dy][z+dz] == 0:
                graph[x+dx][y+dy][z+dz] = graph[x][y][z] + 1
                nv.append((x+dx, y+dy, z+dz))

ans = 0
for i in range(H):
    for j in range(N):
        for k in range(M):
            if graph[i][j][k] == 0:
                print(-1)
                exit()
                
            if graph[i][j][k] > ans:
                ans = graph[i][j][k]

print(ans-1)