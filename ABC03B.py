S = list(input())
T = list(input())
n = len(S)
atcoder = list('atcoder')

for i in range(n):
    if S[i] == '@' and T[i] =='@':
        S[i] = 'a'
        T[i] = 'a'
    elif S[i]=='@':
        if T[i] in atcoder:
            S[i] = T[i]
    elif T[i] == '@':
        if S[i] in atcoder:
            T[i] = S[i]

if T == S:
    res = 'You can win'
else:
    res = 'You will lose'

print(res)
        
        

