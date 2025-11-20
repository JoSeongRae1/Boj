N, M = map(int, input().split())
graph = [list(input()) for i in range(N)]

nv = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 'I':
            nv.append((i, j))

ans = 0
d = [(-1, 0), (1, 0), (0, 1), (0, -1)]
while nv:
    x, y = nv.pop()
    for dx, dy in d:
        if 0 <= x+dx < N and 0 <= y+dy < M and graph[x+dx][y+dy] != '@':
            if graph[x+dx][y+dy] == 'P':
                ans += 1
            if graph[x+dx][y+dy] != 'X':
                graph[x+dx][y+dy] = '@'
                nv.append((x+dx, y+dy))

print(ans if ans > 0 else "TT")