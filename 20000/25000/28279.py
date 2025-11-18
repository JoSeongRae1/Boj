from collections import deque
import sys

D = deque()
N = int(sys.stdin.readline())
for q in range(N):
    S = sys.stdin.readline().split()
    if S[0] == '1':
        D.appendleft(int(S[1]))
    elif S[0] == '2':
        D.append(int(S[1]))
    elif S[0] == '3':
        print(D.popleft() if len(D) > 0 else -1)
    elif S[0] == '4':
        print(D.pop() if len(D) > 0 else -1)
    elif S[0] == '5':
        print(len(D))
    elif S[0] == '6':
        print(1 if len(D) == 0 else 0)
    elif S[0] == '7':
        print(D[0] if len(D) > 0 else -1)
    elif S[0] == '8':
        print(D[-1] if len(D) > 0 else -1)