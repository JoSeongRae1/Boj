import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
A = [0] + [int(sys.stdin.readline().rstrip()) for i in range(N)]
tree_min = [0] + [0 for i in range(N*4)]
tree_max = [0] + [0 for i in range(N*4)]

def min_init(start, end, i):
    if start == end:
        tree_min[i] = A[start]
    else:
        mid = (start + end) // 2
        tree_min[i] = min(min_init(start, mid, i*2), min_init(mid+1, end, i*2+1))
    return tree_min[i]

def min_query(start, end, i, left, right):
    if left > end or right < start:
        return 1000000000+1
    elif left <= start and end <= right:
        return tree_min[i]
    
    mid = (start + end) // 2
    return min(min_query(start, mid, i*2, left, right), min_query(mid+1, end, i*2+1, left, right))

def max_init(start, end, i):
    if start == end:
        tree_max[i] = A[start]
    else:
        mid = (start + end) // 2
        tree_max[i] = max(max_init(start, mid, i*2), max_init(mid+1, end, i*2+1))
    return tree_max[i]

def max_query(start, end, i, left, right):
    if left > end or right < start:
        return -1
    elif left <= start and end <= right:
        return tree_max[i]
    
    mid = (start + end) // 2
    return max(max_query(start, mid, i*2, left, right), max_query(mid+1, end, i*2+1, left, right))

min_init(1, N, 1)
max_init(1, N, 1)

for _ in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    print(min_query(1, N, 1, a, b), max_query(1, N, 1, a, b))