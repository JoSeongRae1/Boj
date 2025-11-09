dp = [0, 1, 2, 4, 7, 13, 24, 44]

k = 7
for tc in range(int(input())):
    n = int(input())
    if k >= n:
        print(dp[n])
    else:
        for i in range(k+1, n+1):
            dp.append(dp[i-3] + dp[i-2] + dp[i-1])
            k += 1

        print(dp[n])