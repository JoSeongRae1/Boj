from collections import Counter

S = input()
print(S.count("JOI"))
ans = 0
for i in range(len(S)-2):
    if (S[i], S[i+1], S[i+2]) == ('I', 'O', 'I'):
        ans += 1
print(ans)