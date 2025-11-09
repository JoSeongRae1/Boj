while True:
    w, h = map(int, input().split())
    if w == h == 0:
        break

    graph = []
    for _ in range(h):
        graph.append(list(map(int, input().split())))

    deltax = [1, 1, 1, -1, -1, -1, 0, 0, 0]
    deltay = [1, 0, -1, 1, 0, -1, 1, 0, -1]
    ans = 0
    for i in range(h):
        for j in range(w):
            nv = []
            v = []
            if graph[i][j] == 1:
                nv.append((i, j))
                while nv:
                    x, y = nv.pop()
                    graph[x][y] = 2
                    for dx, dy in zip(deltax, deltay):
                        if 0 <= x+dx < h and 0 <= y+dy < w and graph[x+dx][y+dy] == 1:
                            nv.append((x+dx, y+dy))
                ans += 1
                    
    
    print(ans)