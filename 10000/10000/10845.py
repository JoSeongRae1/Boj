from collections import deque
N = int(input())
D = deque()
for i in range(N):
    C = input().split()
    if C[0] == "push":
        D.append(int(C[1]))
    elif C[0] == "pop":
        print(D.popleft() if len(D) > 0 else -1)
    elif C[0] == "size":
        print(len(D))
    elif C[0] == "empty":
        print(1 if len(D) == 0 else 0)
    elif C[0] == "front":
        print(D[0] if len(D) > 0 else -1)
    elif C[0] == "back":
        print(D[-1] if len(D) > 0 else -1)