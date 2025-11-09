A = list(set(input() for _ in range(int(input()))))
A.sort(key=lambda x: (len(x), x))
for v in A:
    print(v)