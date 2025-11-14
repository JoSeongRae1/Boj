dp = [0, 1, 1]
n = int(input())
k = 2

while k < n:
    dp.append((dp[k] + dp[k-1]) % 1000000007)
    k += 1

print(dp[n])