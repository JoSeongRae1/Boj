N = int(input())
A = list(map(int, input().split()))
T, P = map(int, input().split())


ans = 0
for i in A:
    if i % T == 0 :
        ans += i // T
    else:
        ans += i // T + 1

print(ans)
print(N//P, N%P)