S = list(input())
for i in range(26):
    try:
        x = chr(97+i)
        print(S.index(x), end=' ')
    except:
        print(-1, end=' ')