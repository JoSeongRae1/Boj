N = int(input())
A = [list(map(int, input().split())) for i in range(N)]
A.sort(key=lambda x:(x[1], x[0]))
ans = 0
E = 0
for a in A:
    s, e = a
    if s >= E:
        ans += 1
        E = e
print(ans)