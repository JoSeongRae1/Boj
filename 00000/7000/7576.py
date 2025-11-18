from collections import deque

M, N = map(int, input().split())
graph = [list(map(int, input().split())) for i in range(N)]

nv = deque()
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            nv.append((i, j))

d = [(-1, 0), (1, 0), (0, 1), (0, -1)]
while nv:
    x, y = nv.popleft()
    for dx, dy in d:
        if 0 <= x+dx < N and 0 <= y+dy < M and graph[x+dx][y+dy] == 0:
            graph[x+dx][y+dy] = graph[x][y] + 1
            nv.append((x+dx, y+dy))

ans = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            ans = -1
            break
        elif graph[i][j] > ans:
            ans = graph[i][j]
    if ans == -1:
        break

print(ans if ans <= 0 else ans-1)