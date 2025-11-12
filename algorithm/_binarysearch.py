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