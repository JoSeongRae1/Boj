v = set()
for t in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x2-x1):
        for y in range(y2-y1):
            v.add((x1 + x, y1 + y))
print(len(v))