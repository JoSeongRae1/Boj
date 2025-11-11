def gcd(a, b):
    while b > 0:
        a, b = b, a%b
    return a

N, M = map(int, input().split())

g = gcd(N, M)
print(g)
print(N*M // g)