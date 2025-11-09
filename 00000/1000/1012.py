T = int(input())

CT = [(1, 0), (-1, 0), (0, 1), (0, -1)]
def dfs(sx, sy):
    need_visited = [(sx, sy)]
    while need_visited:
        x, y = need_visited.pop()
        graph[x][y] = 2
        for ax, ay in CT:
            if 0 <= x+ax < M and 0 <= y+ay < N and graph[x+ax][y+ay] == 1:
                need_visited.append((x+ax, y+ay))

for testcase in range(T):
    M, N, K = map(int, input().split())
    graph = [[0 for i in range(N)] for j in range(M)]
    for _ in range(K):
        x, y = map(int, input().split())
        graph[x][y] = 1

    ans = 0
    for i in range(M):
        for j in range(N):
            if graph[i][j] == 1:
                dfs(i, j)
                ans += 1

    print(ans)