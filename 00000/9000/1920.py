def search(array, k, start, end):
    if end < start:
        return None
    mid = (start + end) // 2

    if array[mid] == k:
        return mid
    elif array[mid] > k:
        return search(array, k, start, mid-1)
    else:
        return search(array, k, mid+1, end)

N = int(input())
A = list(map(int, input().split()))
M = int(input())
X = list(map(int, input().split()))
A.sort()
for x in X:
    if search(A, x, 0, N-1) == None:
        print(0)
    else:
        print(1)