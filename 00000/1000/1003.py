import sys

dp = {0: (1, 0), 1: (0, 1)}
k = 2
for testcase in range(int(sys.stdin.readline().rstrip())):
    a = int(sys.stdin.readline().rstrip())

    if a in dp:
        print(dp[a][0], dp[a][1])
    else:
        for i in range(k, a+1):
            b = dp[i-1]
            c = dp[i-2]
            dp[i] = (b[0] + c[0], b[1] + c[1])
            k += 1
        print(dp[a][0], dp[a][1])