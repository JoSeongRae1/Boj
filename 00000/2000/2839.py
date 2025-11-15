N = int(input())

ans = 0
while N > 0:
    ans += 1
    if N >= 5 and N % 3 != 0:
        N -= 5
    elif N >= 3:
        N -= 3
    elif N < 3:
        ans = -1
        break
print(ans)