ans = 0
for _ in range(N:=int(input())):
    used = set()
    last = None
    for s in input():
        if s in used and s != last:
            ans += 1
            break
        
        last = s
        used.add(s)
print(N-ans)