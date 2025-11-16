N = int(input())

ans = 0
while N > 0:
    ans += 1
    if N >= 5 and N % 2 != 0 or N % 5 == 0:
        N -= 5
    elif N >= 2:
        N -= 2
    elif N < 2:
        ans = -1
        break
print(ans)