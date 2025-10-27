import sys

n = int(input())
A = []
for _ in range(n):
    A.append(int(sys.stdin.readline()))

A.sort()

for i in A:
    print(i)