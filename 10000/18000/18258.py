from collections import deque
import sys

D = deque()
N = int(sys.stdin.readline())
for q in range(N):
    S = sys.stdin.readline().split()
    if S[0] == 'push':
        D.append(int(S[1]))
    elif S[0] == 'pop':
        print(D.popleft() if len(D) > 0 else -1)
    elif S[0] == 'size':
        print(len(D))
    elif S[0] == 'empty':
        print(1 if len(D) == 0 else 0)
    elif S[0] == 'front':
        print(D[0] if len(D) > 0 else -1)
    elif S[0] == 'back':
        print(D[-1] if len(D) > 0 else -1)