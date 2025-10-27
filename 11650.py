A = [tuple(map(int, input().split())) for _ in range(int(input()))]
A.sort(key=lambda x: (x[0], x[1]))
for v in A:
    print(v[0], v[1])