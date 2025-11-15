fibo = [0, 1, 1]
k = 2

N = int(input())
    
while k < N:
    fibo.append(fibo[k-1] + fibo[k])
    k += 1

print(fibo[N])