import sys

S = set()
for _ in range(int(sys.stdin.readline().rstrip())):
    I = sys.stdin.readline().rstrip().split()
    if I[0] == "add":
        S.add(I[1])
    elif I[0] == "remove":
        if I[1] in S:
            S.remove(I[1])
    elif I[0] == "check":
        print(1 if I[1] in S else 0)
    elif I[0] == "toggle":
        if I[1] in S:
            S.remove(I[1])
        else:
            S.add(I[1])
    elif I[0] == "all":
        S = set([f'{i+1}' for i in range(20)])
        print(S)
    elif I[0] == "empty":
        S = set()