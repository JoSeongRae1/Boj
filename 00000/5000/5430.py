import sys
from collections import deque
T = int(sys.stdin.readline())
for testcase in range(T):
    p = list(sys.stdin.readline())
    n = int(sys.stdin.readline())
    S = sys.stdin.readline().replace("[", "").replace("]", "")
    X = deque(map(int, S.split(","))) if n > 0 else []
    R = False
    for q in p:
        if q == 'D':
            if len(X) > 0:
                if R == False:
                    X.popleft()
                else:
                    X.pop()
            else:
                print("error")
                break
        elif q == 'R':
            if R == False:
                R = True
            else:
                R = False
    else:
        if R == True:
            X = reversed(X)
        print(f'[{",".join(map(str, X))}]')