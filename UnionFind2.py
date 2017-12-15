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
        s1 = self.find(x)
        s2 = self.find(y)
        
        if s1 != s2:
            #グラフの長さが異なる場合,長いほうに小さいほうを結合してもグラフの長さは変わらない
            #なので,小さいほうの根を大きいほうの根を参照させるようにすればいい
            
            if self.table[s1] <= self.table[s2]:
                self.table[s2] = s1
            else:
                self.table[s1] = s2
        else:
            #グラフの長さが同じ場合,どちらを根にしても変わらない
            #その際,グラフが1長くなることを考慮する
            self.table[s1] -= 1
            self.table[s2] = s1

        return


G = UnionFind(100)
G.union(1,5)

G2 = UnionFind(100)
G2.union(1,3)
G2.union()