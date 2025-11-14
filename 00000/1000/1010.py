dp = {}
def factorial(n):
    if n not in dp:
        dp[n] = n * factorial(n-1) if n > 1 else 1
    return dp[n]

for testcase in range(int(input())):
    N, M = map(int, input().split())
    C = factorial(M)//(factorial(N)*factorial(M-N))
    print(C)