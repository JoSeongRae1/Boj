dp = [1, 1, 1]

for testcase in range(int(input())):
    N = int(input())

    if len(dp) < N:
        for i in range(len(dp), N):
            dp.append(dp[i-3] + dp[i-2])

    print(dp[N-1])