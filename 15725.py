S = input()
if "x" in S:
    if S.split("x")[0] == '':
        print('1')
    elif S.split("x")[0] == '-':
        print('-1')
    else:
        print(S.split("x")[0])
else:
    print(0)