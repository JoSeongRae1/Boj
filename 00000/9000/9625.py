dp = {0: (1, 0)}

N = int(input())
k = 0
while k < N:
    k += 1
    dp[k] = (dp[k-1][1], dp[k-1][0] + dp[k-1][1])
print(dp[N][0], dp[N][1])