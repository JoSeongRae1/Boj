N = 10
A = [0] + [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tree = [0] + [0 for _ in range(N*4)]

def init(start, end, i):
    if start == end:
        tree[i] = A[start]
    else:
        mid = (start + end) // 2
        tree[i] = init(start, mid, i*2) + init(mid+1, end, i*2+1)
    return tree[i]

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

init(1, 10, 1)

print(tree)

print(query(1, 10, 1, 3, 7))

update(1, 10, 1, 5, 10)

print(tree)