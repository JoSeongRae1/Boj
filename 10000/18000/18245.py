i = 2
while True:
    S = input()
    if S == 'Was it a cat I saw?':
        break

    print(S[::i])
    
    i += 1