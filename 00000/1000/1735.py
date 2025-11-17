def gcd(a, b):
    while b > 0:
        a, b = b, a%b
    return a

a, b = map(int, input().split())
c, d = map(int, input().split())

m = a*d + b*c
n = b*d

g = gcd(m, n)
print(m//g, n//g)