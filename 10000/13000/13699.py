dp = [1]
k = 0
n = int(input())

while k < n:
    k += 1
    s = 0
    for i in range(k):
        s += dp[i]*dp[k-i-1]
    dp.append(s)
print(dp[n])