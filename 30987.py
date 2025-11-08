x1, x2 = map(int, input().split())
a, b, c, d, e = map(int, input().split())
def G(x):
    return 1/3 * a * x**3 + 1/2 * (b-d) * x**2 + (c-e) * x
print(int(G(x2) - G(x1)))