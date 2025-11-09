import sys

N = int(sys.stdin.readline().rstrip())
A = [0] + list(map(int, sys.stdin.readline().rstrip().split()))
M = int(sys.stdin.readline().rstrip())
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

def update(start, end, i, n, k):
    if n < start or n > end:
        pass
    elif start == end == n:
        tree[i] = k
    else:
        mid = (start + end) // 2
        tree[i] = min(update(start, mid, i*2, n, k), update(mid+1, end, i*2+1, n, k))
    return tree[i]

init(1, N, 1)
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    if a == 1:
        update(1, N, 1, b, c)
    else:
        print(query(1, N, 1, b, c))