N = int(input())
A = [0] + list(map(int, input().split()))
tree = [0] + [0 for i in range(N*4)]

def init(start, end, i):
    if start == end:
        tree[i] = (A[start], start)
    else:
        mid = (start + end) // 2
        l = init(start, mid, i*2)
        r = init(mid+1, end, i*2+1)
        if l[0] > r[0]:
            tree[i] = r
        elif l[0] < r[0]:
            tree[i] = l
        else:
            tree[i] = (l[0], min(l[1], r[1]))

    return tree[i]

def query(start, end, i, left, right):
    if right < start or end < left:
        return (1000000001, 100001)
    if left <= start and end <= right:
        return tree[i]
    mid = (start + end) // 2
    l = query(start, mid, i*2, left, right)
    r = query(mid+1, end, i*2+1, left, right)
    if l[0] > r[0]:
        return r
    elif l[0] < r[0]:
        return l
    else:
        if l[1] > r[1]:
            return r
        else:
            return l

def update(start, end, i, n, k):
    if n < start or end < n:
        pass
    elif start == end == n:
        tree[i] = (k, n)
    else:
        mid = (start + end) // 2
        l = update(start, mid, i*2, n, k)
        r = update(mid+1, end, i*2+1, n, k)
        if l[0] > r[0]:
            tree[i] = r
        elif l[0] < r[0]:
            tree[i] = l
        else:
            tree[i] = (l[0], min(l[1], r[1]))
    
    return tree[i]

init(1, N, 1)

M = int(input())
for q in range(M):
    a, b, c = map(int, input().split())
    if a == 1:
        update(1, N, 1, b, c)
    else:
        print(query(1, N, 1, b, c)[1])