N = int(input())

ans = 0
for x in range(1, N+1):
    S = list(map(int, list(str(x))))
    
    if len(S) == 1:
        ans += 1
        continue

    d = S[1] - S[0]

    k = True
    for i in range(len(S)-1):
        if S[i+1] - S[i] != d:
            k = False

    if k == True:
        ans += 1
print(ans)