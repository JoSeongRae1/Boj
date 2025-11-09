ans = 0

for _ in range(int(input())):
    C, K = map(int, input().split())
    ans += C * K

print(ans)