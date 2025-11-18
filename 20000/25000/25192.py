N = int(input())
ans = 0
S = set()
for q in range(N):
    s = input()
    if s == 'ENTER':
        S.clear()
    else:
        if s not in S:
            S.add(s)
            ans += 1

print(ans)