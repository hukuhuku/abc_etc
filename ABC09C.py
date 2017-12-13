N,K = list(map(int,input().split()))
S = input()


res = list(S)
list_S = list(S)
sort_S = sorted(list_S)

a = []

for i in range(N):

    if res[i] != sort_S[i]:
        if (sort_S[i] in a or res[i] in a) and 1 <= K:
            
            index = res.index(sort_S[i])
            b = res[i]
            res[i] = sort_S[i]
            res[index] = b
            a.append(b)
            a.append(sort_S[i])
            K-=1                
        elif sort_S[i] in a and res[i] in a:
            index = res.index(sort_S[i])
            b = res[i]
            res[i] = sort_S[i]
            res[index] = b
        elif 2 <= K:
            index = res.index(sort_S[i])
            b = res[i]
            res[i] = sort_S[i]
            res[index] = b
            a.append(b)
            a.append(sort_S)
            K-=2


print("".join(res))           



