N = int(input())
S = list(map(int, list(str(N))))
if sum(S) % 3 == 0 and 0 in S:
    S.sort(reverse=True)
    for i in S:
        print(i, end='')
else:
    print(-1)    