for testcase in range(int(input())):
    S = list(input())
    k = 0
    ans = 0
    for i in S:
        if i == "O":
            k += 1
            ans += k
        else:
            k = 0
    print(ans)