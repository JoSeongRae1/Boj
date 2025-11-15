N = int(input())
A = list(map(int, input().split()))
x = int(input())

A.sort()

ans = 0
start = 0
end = N-1

while True:
    if start == end:
        break

    s = A[start] + A[end]
    if s == x:
        ans += 1
    if s <= x:
        start += 1
    else:
        end -= 1

print(ans)