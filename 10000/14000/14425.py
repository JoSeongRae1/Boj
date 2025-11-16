N, M = map(int, input().split())
S = set([input() for i in range(N)])
ans = 0
for i in range(M):
    s = input()
    if s in S:
        ans += 1
print(ans)