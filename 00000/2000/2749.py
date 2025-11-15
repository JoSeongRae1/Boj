fibo = [0, 1, 1]
k = 2

N = int(input())

while k < 1500000:
    fibo.append((fibo[k-1] + fibo[k]) % 1000000)
    k += 1

print(fibo[N%1500000])