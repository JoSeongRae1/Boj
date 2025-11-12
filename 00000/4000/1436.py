N = int(input())

i = 0
k = 0
while True:
    i += 1
    if "666" in str(i):
        k += 1
        if k == N:
            print(i)
            break