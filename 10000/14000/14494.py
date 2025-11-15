n, m = map(int, input().split())
dp = [[0 for j in range(n)] for i in range(m)]

dp[0][0] = 1

p = 10**9 + 7

for i in range(m):
    for j in range(n):
        if i == j == 0:
            continue

        a, b, c = 0, 0, 0
        if i > 0:
            a = dp[i-1][j]
        if j > 0:
            b = dp[i][j-1]
        if i > 0 and j > 0:
            c = dp[i-1][j-1]

        dp[i][j] = (a + b + c)%p

print(dp[m-1][n-1])