N, M = map(int, input().split())
A = [list(input()) for i in range(N)]


ans = []
for i in range(N-7):
    for j in range(M-7):
        wa = 0
        ba = 0
        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a + b) % 2 == 0:
                    if A[a][b] != 'W':
                        wa += 1
                    else:
                        ba += 1
                else:
                    if A[a][b] != 'W':
                        ba += 1
                    else:
                        wa += 1

        ans.append(wa)
        ans.append(ba)

print(min(ans))