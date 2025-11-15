import sys

N = int(sys.stdin.readline())
A = [0] + list(map(int, sys.stdin.readline().split()))
tree = [0] + [0 for i in range(N*4)]

def init(start, end, i):
    if start == end:
        tree[i] = (A[start], A[start])
    else:
        mid = (start + end) // 2
        l = init(start, mid, i*2)
        r = init(mid+1, end, i*2+1)
        tree[i] = (l[0] + r[0], min(l[1], r[1]))
    return tree[i]

def query(start, end, i, left, right):
    if right < start or end < left:
        return (0, 2000001)
    if left <= start and end <= right:
        return tree[i]
    mid = (start + end) // 2
    l = query(start, mid, i*2, left, right)
    r = query(mid+1, end, i*2+1, left, right)
    return (l[0] + r[0], min(l[1], r[1]))

init(1, N, 1)

ans = 0
for i in range(1, N+1):
    for j in range(i+1, N+1):
        qu = query(1, N, 1, i, j)
        q = qu[0] * qu[1]
        if ans < q:
            ans = q
print(ans if N > 1 else A[1])