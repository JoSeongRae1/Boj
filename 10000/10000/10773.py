K = int(input())
s = []
for q in range(K):
    a = int(input())
    if a == 0:
        s.pop()
    else:
        s.append(a)
print(sum(s))