W = 6
H = 4
N = 3
X = [2,3,4]
Y = [4,1,3]


memo = [[False for i in range(H)]for i in range(W)]

def bfs(x,y,res,memo):
    for dx,dy in [[1,0],[-1,0],[0,1],[0,-1]]:
        if memo[x+dx][y+dy] == False:
            res += 1
            memo[x+dx][y+dy] = True
            if x+dx == H-1 or y+dy == W-1:
                return 
            return bfs(x+dx,y+dy,res,memo)
    return res

bfs(4,2,0,memo)

