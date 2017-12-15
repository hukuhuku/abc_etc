class UnionFind():
    def __init__ (self,size):
        self.table = range(size)#大きさがsizeの配列を作成
    
    def find (self,x):
        return self.table[x]

    def union(self,x,y):
        x1 = self.find(x)
        y1 = self.find(y)
        if x1 == y1:   
            return False
        for i in range(len(self.table)):
            if self.table[i] == y1:
                self.table[i] = x1
        return True