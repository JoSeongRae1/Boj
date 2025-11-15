fibo = [1, 1]
k = 2

for testcase in range(1, int(input())+1):
    P, Q = map(int, input().split())
    
    while k < P:
        fibo.append(fibo[k-1] + fibo[k-2])
        k += 1
    
    print(f'Case #{testcase}: {fibo[P-1] % Q}')