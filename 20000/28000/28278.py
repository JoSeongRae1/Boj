import sys

N = int(sys.stdin.readline())
A = []
for q in range(N):
    S = sys.stdin.readline().split()
    if S[0] == '1':
        A.append(int(S[1]))
    elif S[0] == '2':
        print(A.pop() if len(A) > 0 else -1)
    elif S[0] == '3':
        print(len(A))
    elif S[0] == '4':
        print(1 if len(A) == 0 else 0)
    elif S[0] == '5':
        print(A[-1] if len(A) > 0 else -1)