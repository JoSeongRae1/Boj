for testcase in range(int(input())):
    N = int(input())
    X = list(map(int, input().split()))
    S = [0]
    for i in range(N):
        S.append(S[i] + X[i])

    ans = -9999999999
    for i in range(N):
        for j in range(i+1, N+1):
            if ans < S[j]-S[i]:
                ans = S[j]-S[i]
    print(ans)