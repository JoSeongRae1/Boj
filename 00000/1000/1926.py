import sys

N, M = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for i in range(N)]

ans = 0
max = 0
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
for i in range(N):
    for j in range(M):
        nv = []
        c = 1
        if graph[i][j] == 1:
            ans += 1
            nv.append((i, j))

        while nv:
            x, y = nv.pop()
            if graph[x][y] == 1:
                c += 1
                graph[x][y] = c

            for dx, dy in d:
                if 0 <= x + dx < N and 0 <= y + dy < M and graph[x+dx][y+dy] == 1:
                    nv.append((x+dx, y+dy))

        if c > max:
            max = c

print(ans)
print(max-1)