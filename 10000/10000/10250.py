for testcase in range(int(input())):
    H, W, N = map(int, input().split())
    f = N % H
    l = N // H + 1
    if f == 0:
        f = H
        l -= 1

    print(f * 100 + l)