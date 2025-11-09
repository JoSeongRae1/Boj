import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
A = [0] + [int(sys.stdin.readline().rstrip()) for i in range(N)]
tree = [0] + [0 for i in range(N*4)]

def init(start, end, i):
    if start == end:
        tree[i] = A[start]
    else:
        mid = (start + end) // 2
        tree[i] = min(init(start, mid, i*2), init(mid+1, end, i*2+1))
    return tree[i]

def query(start, end, i, left, right):
    if right < start or end < left:
        return 1000000000+1
    if left <= start and end <= right:
        return tree[i]
    
    mid = (start + end) // 2
    return min(query(start, mid, i*2, left, right), query(mid+1, end, i*2+1, left, right))

init(1, N, 1)

for _ in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    print(query(1, N, 1, a, b))