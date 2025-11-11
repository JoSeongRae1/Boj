import math

def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

N = int(input())
A = list(map(int, input().split()))
ans = 0
for i in A:
    if isPrime(i):
        ans += 1
print(ans)