N, K = map(int, input().split())
A = [int(input()) for i in range(N)]
A.reverse()

ans = 0
while K > 0:
    ans += 1
    for c in A:
        if c <= K:
            K -= c
            break

print(ans)