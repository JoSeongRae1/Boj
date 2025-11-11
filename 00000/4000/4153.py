while True:
    S = list(map(int, input().split()))
    S.sort()

    if S[0] == S[1] == S[2] == 0:
        break

    print("right" if S[2] ** 2 == S[1] ** 2 + S[0] ** 2 else "wrong")