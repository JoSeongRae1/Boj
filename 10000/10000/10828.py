N = int(input())
S = []
for i in range(N):
    c = input().split()
    if c[0] == "push":
        S.append(int(c[1]))
    elif c[0] == "pop":
        print(S.pop() if len(S) > 0 else -1)
    elif c[0] == "size":
        print(len(S))
    elif c[0] == "empty":
        print(1 if len(S) == 0 else 0)
    elif c[0] == "top":
        print(S[-1] if len(S) > 0 else -1)