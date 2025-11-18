N = int(input())
C = []
for q in range(N):
    x, y = map(int, input().split())
    C.append((x, y))
C.append(C[0])
N += 1

a, b = 0, 0
for i in range(N-1):
    a += C[i][0]*C[i+1][1]
    b += C[i+1][0]*C[i][1]

print(round(abs(a-b)/2, 1))