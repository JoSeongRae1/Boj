N, M = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
for i in A:
    for j in A:
        for k in A:
            if i != j and j != k and i != k and ans < i+j+k <= M:
                ans = i+j+k
print(ans)