S = input()
S = S.replace('XXXX', 'AAAA')
S = S.replace('XX', 'BB')
print(S if 'X' not in S else -1)