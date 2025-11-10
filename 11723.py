import sys

S = set()

for _ in range(int(sys.stdin.readline().rstrip())):
    s = sys.stdin.readline().rstrip().split()
    if len(s) == 1:
        a = s[0]
    else:
        a = s[0]
        b = int(s[1])
    
    if a == "add":
        S.add(b)
    elif a == "remove":
        if b in S:
            S.remove(b)
    elif a == "check":
        print(1 if b in S else 0)
    elif a == "toggle":
        if b in S:
            S.remove(b)
        else:
            S.add(b)
    elif a == "all":
        S = set([i for i in range(1, 21)])
    elif a == "empty":
        S = set()