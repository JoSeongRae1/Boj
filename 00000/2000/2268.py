import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
A = [0] + [0 for i in range(N)]
tree = [0] + [0 for i in range(N*4)]

def query(start, end, i, left, right):
    if right < start or end < left:
        return 0
    if left <= start and end <= right:
        return tree[i]
    mid = (start + end) // 2
    return query(start, mid, i*2, left, right) + query(mid+1, end, i*2+1, left, right)

def update(start, end, i, n, k):
    if n < start or end < n:
        pass
    elif start == end == n:
        tree[i] = k
    else:
        mid = (start + end) // 2
        tree[i] = update(start, mid, i*2, n, k) + update(mid+1, end, i*2+1, n, k)
    return tree[i]  

for i in range(M):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())


    if a == 0:
        if b > c:
            t = b
            b = c
            c = t
        print(query(1, N, 1, b, c))
    else:
        update(1, N, 1, b, c)