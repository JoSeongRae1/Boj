N = int(input())
A = []
for _ in range(N):
    i, j = input().split()
    A.append([int(i), j])
A.sort(key=lambda x: x[0])
for v in A:
    print(v[0], v[1])