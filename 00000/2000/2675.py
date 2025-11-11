for testcase in range(int(input())):
    a, b = input().split()
    c = int(a)

    s = list(b)
    for i in s:
        print(i*c, end="")
    print("")