dp = [1, 1, 1]
n = int(input())
k = 3
while k < n:
    k += 1
    dp.append(dp[k-4] + dp[k-2])
print(dp[n-1])