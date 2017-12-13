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

N,M = list(map(int,input().split()))
A = []
B = []
for i in range(M):
    a,b = map(int,input().split())
    A.append(a-1)
    B.append(b-1)

res = 0

for i in range(M):
    G = UnionFind(N)
    for j in range(M):
        if i != j:
            G.union(A[j],B[j])
    minas = 0
    for k in G.table:
        if k < 0:
            minas += 1
    if minas == 1:
        res += 1


print(M-res)
        