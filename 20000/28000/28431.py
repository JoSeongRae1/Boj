A = [0 for i in range(10)]

for i in range(5):
    A[int(input())] += 1

for i in range(10):
    if A[i] % 2 == 1:
        print(i) 