N = int(input())

ans = 0
for i in range(1, 1000001):
    S = list(map(int, list(str(i))))
    if sum(S) + i == N:
        ans = i
        break
print(ans)