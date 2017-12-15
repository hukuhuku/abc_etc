def find(x):
    #与えられた頂点の根のindexを取得する
    while table[x] >= 0:
        x = table[x]
    return x

def union(x,y):
    global table
    s1 = find(x)
    s2 = find(y)
    if s1 != s2:
        if table[s1] != table[s2]:
            #与えられた頂点の根が異なる場合
            if table[s1] < table[s2]:
                table[s2] = s1
            else:
                table[s1] = s2
        else:
            #グラフの長さが同じ場合,どちらを根にしても変わらない
            #その際,グラフが1長くなることを考慮する
            table[s1] += -1
            table[s2] = s1
    return

N,Q = list(map(int,input().split()))
table = [-1 for i in range(N)]
res = []


for i in range(Q):
    P,A,B = list(map(int,input().split()))
    if P == 1:
        r1 = find(A)
        r2 = find(B)
        if r1 == r2:
            res.append('Yes')
        else:    
            res.append('No')
    else:
        union(A,B)

for i in res:
    print(i)