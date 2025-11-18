N = int(input())
D = {}
K = []
for i in range(N):
    S = input()
    if S not in D:
        D[S] = 0
        K.append(S)
    D[S] += 1

K.sort(key=lambda x: (-D[x], x))

print(K[0])