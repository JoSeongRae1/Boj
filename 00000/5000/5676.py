def init(start, end, i):
    if start == end:
        tree[i] = X[start]
    else:
        mid = (start + end) // 2
        tree[i] = init(start, mid, i*2) * init(mid+1, end, i*2+1)
    return tree[i]

def query(start, end, i, left, right):
    if right < start or end < left:
        return 1
    if left <= start and end <= right:
        return tree[i]
    mid = (start + end) // 2
    return query(start, mid, i*2, left, right) * query(mid+1, end, i*2+1, left, right)

def update(start, end, i, n, k):
    if n < start or end < n:
        pass
    elif start == end == n:
        tree[i] = k
    else:
        mid = (start + end) // 2
        tree[i] = update(start, mid, i*2, n, k) * update(mid+1, end, i*2+1, n, k)
    return tree[i]

while True:
    try:
        N, K = map(int, input().split())
        X = [0] + list(map(lambda x: 1 if int(x) > 0 else (0 if int(x) == 0 else -1), input().split()))
        tree = [0] + [0 for i in range(N*4)]

        init(1, N, 1)

        ans = ""
        for _ in range(K):
            a, b, c = input().split()
            if a == 'C':
                i = int(b)
                V = int(c)

                if V > 0:
                    V = 1
                elif V == 0:
                    V = 0
                else:
                    V = -1

                update(1, N, 1, i, V)
            else:
                i = int(b)
                j = int(c)
                s = query(1, N, 1, i, j)
                if s > 0:
                    ans += '+'
                elif s == 0:
                    ans += '0'
                else:
                    ans += '-'
        if ans != "":
            print(ans)
    except:
        break