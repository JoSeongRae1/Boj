def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

N = int(input())
for q in range(N):
    ans = 0
    A = list(map(int, input().split()))
    del A[0]
    l = len(A)
    for i in range(l):
        for j in range(i+1, l):
            ans += gcd(A[i], A[j])
    print(ans)