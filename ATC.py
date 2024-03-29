class UnionFind():
    #負の値はルートで集合の個数
    #正の値は次の要素を返す
    def __init__(self,size):
        self.table = [-1 for _  in range(size)]
    
    #集合の代表を求める
    def find(self,x):
        while self.table[x] >= 0:
            #根に来た時,self.table[根のindex]は負の値なのでx = 根のindexで値が返される。
            x = self.table[x]
        return x
    
    #併合
    def union(self,x,y):
        s1 = self.find(x)#根のindex,table[s1]がグラフの高さ
        s2 = self.find(y)
        if s1 != s2:#根が異なる場合
            if self.table[s1] != self.table[s2]:#グラフの高さが異なる場合
                if self.table[s1] < self.table[s2]:
                    self.table[s2] = s1
                else:
                    self.table[s1] = s2
            else:
                #グラフの長さが同じ場合,どちらを根にしても変わらない
                #その際,グラフが1長くなることを考慮する
                self.table[s1] += -1
                self.table[s2] = s1
        return

N,Q = map(int,input().split())
G = UnionFind(N)
res = []
for i in range(Q):
    P,A,B = map(int,input().split())
    if P == 1:
        if G.find(A) == G.find(B):
            res.append('Yes')
        else:
            res.append('No')
    else:
        if A != B:#自己ループは実装しない
            G.union(A,B)


for s in res:
    print(s)