from collections import deque

N = int(input())
D = deque(range(1, N+1))

while len(D) > 1:
    D.popleft()
    D.append(D.popleft())
print(D[0])