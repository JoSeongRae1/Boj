R, C = map(int, input().split())
graph = []

for _ in range(R):
    graph.append(list(input()))

ans_o, ans_v = 0, 0
d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
need_visited = []
for i in range(R):
    for j in range(C):
        if graph[i][j] != '#':
            o, v = 0, 0
            need_visited.append((i, j))
            while need_visited:
                x, y = need_visited.pop()
                if graph[x][y] == 'o':
                    o += 1
                elif graph[x][y] == 'v':
                    v += 1
                graph[x][y] = '@'
                
                for dx, dy in d:
                    if 0 <= x + dx < R and 0 <= y + dy < C:
                        if graph[x+dx][y+dy] != '#' and graph[x+dx][y+dy] != '@':
                            need_visited.append((x+dx, y+dy))
                    else:
                        need_visited.clear()

            if o > v:
                ans_o += o
            else:
                ans_v += v
print(ans_o, ans_v)