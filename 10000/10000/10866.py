from collections import deque

N = int(input())
D = deque()
for q in range(N): 
    C = input().split()
    if C[0] == 'push_front':
        D.appendleft(int(C[1]))

    if C[0] == 'push_back':
        D.append(int(C[1]))

    if C[0] == 'pop_front':
        print(D.popleft() if len(D) > 0 else -1)

    if C[0] == 'pop_back':
        print(D.pop() if len(D) > 0 else -1)

    if C[0] == 'size':
        print(len(D))

    if C[0] == 'empty':
        print(1 if len(D) == 0 else 0)
    
    if C[0] == 'front':
        print(D[0] if len(D) > 0 else -1)

    if C[0] == 'back':
        print(D[-1] if len(D) > 0 else -1)